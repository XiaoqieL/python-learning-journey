from unittest.mock import Mock


class LightController:
    def __init__(self, serial_port):
        self.serial = serial_port  # 依赖串口对象

    def turn_on(self):
        """开灯：发 ON 命令"""
        self.serial.write(b"ON\n")

    def turn_off(self):
        """关灯：发 OFF 命令"""
        self.serial.write(b"OFF\n")

    def get_status(self):
        """查询状态：发 STATUS，读回复"""
        self.serial.write(b"STATUS\n")
        return self.serial.read().strip()


def test_turn_on():
    """开灯命令是否正确发送"""
    fake_serial = Mock
    light = LightController(fake_serial)

    light.turn_on()

    # 断言：串口的 write 方法被调用了1次，参数是 b"ON\n"
    fake_serial.write.assert_called_once_with(b"ON\n")


def test_turn_off():
    """关灯命令是否发送正确"""
    fake_serial = Mock
    light = LightController(fake_serial)

    light.turn_off()

    # 断言：串口的 write 方法被调用了1次，参数是 b“ON\n”
    fake_serial.write.assert_called_once_with(b"OFF\n")


def test_get_status():
    """查询状态时是否返回串口的回复"""
    fake_serial = Mock()
    # 预设：read() 会返回 b"ON\r\n"(模拟灯是亮的)
    fake_serial.read.return_value = b"ON\r\n"

    light = LightController(fake_serial)
    result = light.get_status()

    assert result == b"ON"
    # 再断言一下：发出去的命令是对的
    fake_serial.write.assert_called_called_with(b"STATUS\n")
