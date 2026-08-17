# 接口请求封装
import requests
import logging
from day33_test_project.config import Config

logger = logging.getLogger(__name__)


class APIHelper:
    def __init__(self, base_url=Config.BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, params=None):
        url = f"{self.base_url}{path}"
        logger.info(f"GET {url}")
        resp = self.session.get(url, params=params, timeout=Config.TIMEOUT)
        logger.info(f"→{resp.status_code}")
        return resp

    def post(self, path, json_data=None):
        url = f"{self.base_url}{path}"
        logger.info(f"POST {url}")
        resp = self.session.post(url, json=json_data, timeout=Config.TIMEOUT)
        logger.info(f"→ {resp.status_code}")
        return resp

    def delete(self, path):
        url = f"{self.base_url}{path}"
        resp = self.session.delete(url, timeout=Config.TIMEOUT)
        return resp
