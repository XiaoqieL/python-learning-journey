import time
from unittest.mock import Mock, patch
import pytest


class LightPowerTester:
    """智能灯具断上电测试器"""

    def __init__(self, serial_port, power_off_delay=3, power_on_delay=6):
        self.serial = serial_port
        self.power_off_delay = power_off_delay  # 断电后等多久
        self.power_on_delay = power_on_delay  # 上电等多久
        self.test_count = 0
        self.pass_count = 0
        self.fail_count = 0

    def power_off(self):
        """断电：发 RELAY OFF 命令"""
        self.serial.write(b"RELAY OFF\n")

    def power_on(self):
        """上电: 发 RELAY ON 命令"""
        self.serial.write(b"RELAY ON\n")

    def check_status(self):
        """查询灯具状态，返回 ON 或 OFF"""
        self.serial.write(b"STATUS\n")
        resp = self.serial.read().strip()
        return resp.decode()  # bytes 转字符串

    def run_one_cycle(self, expected_after_on="ON"):
        """执行一轮断上电测试：断电→等→上电→等→检查
        返回 True（通过）/False(失败)"""
        self.test_count += 1

        # 断电
        self.power_off()
        time.sleep(self.power_off_delay)

        # 上电
        self.power_on()
        time.sleep(self.power_on_delay)

        # 检查
        status = self.check_status()
        if status == expected_after_on:
            self.pass_count += 1
            return True
        else:
            self.fail_count += 1
            return False


@pytest.fixture
def fake_serial():
    """造一个 Mock 串口"""
    s = Mock()
    s.read.return_value = b"ON\r\n"  # 默认回复 ON (灯是亮的)
    return s


@pytest.fixture
def tester(fake_serial):
    """造一个测试器，用假串口"""
    return LightPowerTester(fake_serial, power_off_delay=0, power_on_delay=0)


# 为什么 delay 设成 0？——测试里`time.sleep` 会浪费时间，设 0 让测试秒跑完。这就是"测试用和生产用参数不一样"的典型做法。

def test_power_off_sends_correct_command(tester, fake_serial):
    tester.power_off()
    fake_serial.write.assert_called_with(b"RELAY OFF\n")


def test_power_on_sends_correct_command(tester, fake_serial):
    tester.power_on()
    fake_serial.write.assert_called_with(b"RELAY ON\n")


def test_one_cycle_pass(tester, fake_serial):
    result = tester.run_one_cycle("ON")
    assert result is True
    assert tester.test_count == 1
    assert tester.pass_count == 1
    assert tester.fail_count == 0
    # write 被调用了几次？断电1次 + 上电1次 + 查询1次 = 3次
    assert fake_serial.write.call_count == 3


def test_one_cycle_fail(tester, fake_serial):
    # 模拟灯坏了，上电后还是 OFF
    fake_serial.read.return_value = b"OFF\r\n"

    result = tester.run_one_cycle("ON")
    assert result is False
    assert tester.fail_count == 1
    assert tester.pass_count == 0


# 现在测试里 delay 设 0 有点"作弊"——真实代码里是 3 秒和 6 秒。更好的做法是：保持真实参数， 把`time.sleep` 本身 Mock 掉 ，让它不真的睡。
@patch("time.sleep")
def test_cycle_with_real_delays(mock_sleep, tester, fake_serial):
    """用真实的延时参数，但 sleep 被 Mock 了，测试不真等"""
    # 重新构造 tester，用真实的 delay
    tester2 = LightPowerTester(fake_serial, power_off_delay=3, power_on_delay=6)

    result = tester2.run_one_cycle("ON")

    assert result is True
    # 断言 sleep 被调用了 2 次(断电一次、上电一次)
    assert mock_sleep.call_count == 2
    # 断言第一次睡了 3 秒， 第二次睡了 6 秒
    mock_sleep.assert_any_call(3)
    mock_sleep.assert_any_call(6)

# `@patch` 是 Mock 的高级用法——它临时替换某个模块里的函数/对象，测试结束自动恢复。这是测"包含耗时操作/外部依赖"代码的标准做法
