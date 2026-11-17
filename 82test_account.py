import json
import os
import pytest
from day73_class_decorators import Account, NegativeAmountError

# 注意：如果 import 报错(找不到模块)，就直接把 Account 类复制到这个文件里

TEST_FILE = "test_account_temp.json"  # 测试用的数据文件，别污染正式的


def setup_function():
    """每个测试前执行：确保测试文件不存在，从零开始"""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def teardown_function():
    """每个测试后执行：清理测试文件"""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_empty_account():
    acc = Account(TEST_FILE)
    assert acc.total == 0
    assert len(acc.records) == 0


def test_add_one():
    acc = Account(TEST_FILE)
    acc.add("午饭", 25.5)
    assert acc.total == 25.5
    assert "午饭" in acc.records


def test_add_multiple():
    acc = Account(TEST_FILE)
    acc.add("早饭", 10)
    acc.add("午饭", 25)
    acc.add("晚饭", 30)
    assert acc.total == 65


def test_negative_amount():
    acc = Account(TEST_FILE)
    with pytest.raises(NegativeAmountError):
        acc.add("测试", -100)
