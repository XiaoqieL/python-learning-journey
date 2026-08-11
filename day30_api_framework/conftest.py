
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from api_client import APIClient


@pytest.fixture
def api():
    """每个测试用例都能用的APIClient实例"""
    return APIClient()


@pytest.fixture
def new_user_data():
    """测试数据：新用户"""
    return {
        "name": "小杰",
        "username": "xiaojie",
        "email": "xiaojie@test.com",
        "phone": "138-1234-5678",
        "website": "xiaojie.dev"
    }
