import pytest
from day73_class_decorators import Account, NegativeAmountError


# 注意：如果 import 报错(找不到模块)，就直接把 Account 类复制到这个文件里

@pytest.mark.smoke
def test_empty_account(empty_acc):
    assert empty_acc.total == 0
    assert len(empty_acc.records) == 0


@pytest.mark.smoke
def test_add_one(empty_acc):
    empty_acc.add("午饭", 25.5)
    assert empty_acc.total == 25.5
    assert "午饭" in empty_acc.records


def test_add_multiple(empty_acc):
    empty_acc.add("早饭", 10)
    empty_acc.add("午饭", 25)
    empty_acc.add("晚饭", 30)
    assert empty_acc.total == 65


@pytest.mark.exception
def test_negative_amount(empty_acc):
    with pytest.raises(NegativeAmountError):
        empty_acc.add("测试", -100)
