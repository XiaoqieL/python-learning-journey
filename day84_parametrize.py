import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),  # 第一组
    (10, 20, 30),  # 第二组
    (0, 0, 0),  # 第3组
    (-1, -1, 0),  # 第4组
    (100, 200, 300),  # 第5组
])
def test_add(a, b, expected):
    assert add(a, b) == expected


# ==== 练习2：及格判断参数化 ====

def is_pass(score):
    return score >= 60


@pytest.mark.parametrize("score, expected", [
    (60, True),
    (59, False),
    (0, False),
    (100, True),
    (55, True),
])
def test_is_pass(score, expected):
    assert is_pass(score) == expected
