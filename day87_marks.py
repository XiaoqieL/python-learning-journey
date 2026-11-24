import pytest
import time


@pytest.mark.smoke  # 打标签：冒烟测试
def test_login():
    """登录测试，快速验证主流程"""
    assert 1 + 1 == 2


@pytest.mark.smoke
def test_home_page():
    """首页加载测试"""
    assert "home".upper() == "HOME"


@pytest.mark.slow  # 打标签：慢测试
def test_big_loop():
    """耗时的大数据循环测试"""
    total = 0
    for i in range(1000000):
        total += i
    assert total > 0


@pytest.mark.slow
@pytest.mark.serial  # 一个测试可以打多个标签
def test_serial_comm():
    """串口通信测试(慢 + 串口)"""
    time.sleep(0.1)
    assert True


def test_normal():
    """普通测试，没标签"""
    assert 10 > 5
