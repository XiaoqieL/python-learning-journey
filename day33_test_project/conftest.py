import sys
import os
import pytest
import logging
from playwright.sync_api import sync_playwright
from day33_test_project.config import Config

# 让tests目录导入上层模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)


# ===== 接口测试 fixture =====
@pytest.fixture
def api():
    from utils.api_helper import APIHelper
    client = APIHelper()
    yield client


# ===== UI测试 fixture =====
@pytest.fixture
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=Config.HEADLESS)
        page = browser.new_page()
        yield page
        browser.close()


# ===== 测试数据 fixture =====
@pytest.fixture
def user_data():
    from utils.data_helper import load_csv
    return load_csv("users.csv")
