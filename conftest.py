import os
import pytest
from day73_class_decorators import Account

TEST_FILE = "test_account_temp.json"


@pytest.fixture
def empty_acc():
    """返回一个空的 Account 对象，测试完自动清理文件"""
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    acc = Account(TEST_FILE)
    yield acc
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
