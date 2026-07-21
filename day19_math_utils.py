# ============ 第19天：被测试的工具函数 ============

def add(a, b):
    """加法"""
    return a + b


def subtract(a, b):
    """减法"""
    return a - b


def multiply(a, b):
    """乘法"""
    return a * b


def divide(a, b):
    """除法，除数为0时抛出异常"""
    if b == 0:
        raise ValueError("除数不能为0")
    return a / b


def is_even(n):
    """判断是否是偶数"""
    return n % 2 == 0


def get_grade(score):
    """根据分数返回等级"""
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"
