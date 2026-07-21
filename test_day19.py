# ============ 第19天：pytest测试用例 ============
# 注意：文件名必须以 test_ 开头，函数名也必须以 test_ 开头

from day19_math_utils import add, subtract, multiply, divide, is_even, get_grade


# --- 基本运算测试 ---
def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(5, 5) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 100) == 0


# ----异常测试---
def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_zero():
    import pytest
    with pytest.raises(ValueError, match="除数不能为0"):
        divide(10, 0)


# --- 偶数判断测试 ---
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-4) == True


# --- 等级测试（多种情况）---
def test_grade_excellent():
    assert get_grade(95) == "优秀"
    assert get_grade(90) == "优秀"


def test_grade_good():
    assert get_grade(85) == "良好"
    assert get_grade(80) == "良好"


def test_grade_pass():
    assert get_grade(70) == "及格"
    assert get_grade(60) == "及格"


def test_grade_fail():
    assert get_grade(55) == "不及格"
    assert get_grade(0) == "不及格"


# ---- 参数化测试（一次测多组数据） ---
import pytest


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 20, 30),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 1, 101),
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected
