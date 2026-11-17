import json
import os
import pytest
from day73_class_decorators import Account, NegativeAmountError

# 注意：如果 import 报错(找不到模块)，就直接把 Account 类复制到这个文件里

TEST_FILE = "test_account_temp.json"  # 测试用的数据文件，别污染正式的


@pytest.fixture
def empty_acc():
    """返回一个空的 Account 对象，测试完自动清理文件"""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    acc = Account(TEST_FILE)
    yield acc  # yield 之前是 setup, 之后是 teardown
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_empty_account(empty_acc):
    assert empty_acc.total == 0
    assert len(empty_acc.records) == 0


def test_add_one(empty_acc):
    empty_acc.add("午饭", 25.5)
    assert empty_acc.total == 25.5
    assert "午饭" in empty_acc.records


def test_add_multiple(empty_acc):
    empty_acc.add("早饭", 10)
    empty_acc.add("午饭", 25)
    empty_acc.add("晚饭", 30)
    assert empty_acc.total == 65


def test_negative_amount(empty_acc):
    with pytest.raises(NegativeAmountError):
        empty_acc.add("测试", -100)
