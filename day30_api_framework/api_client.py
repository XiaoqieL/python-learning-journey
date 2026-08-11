# 接口封装层：把HTTP请求封装成Python方法
import requests
import logging
from config import BASE_URL, TIMEOUT

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path, params=None):
        url = f"{self.base_url}{path}"
        logger.info(f"GET {url} params={params}")
        resp = self.session.get(url, params=params, timeout=TIMEOUT)
        logger.info(f"响应 {resp.status_code}")
        return resp

    def post(self, path, json_data=None):
        url = f"{self.base_url}{path}"
        logger.info(f"POST {url} data={json_data}")
        resp = self.session.post(url, json=json_data, timeout=TIMEOUT)
        logger.info(f"响应 {resp.status_code}")
        return resp

    def put(self, path, json_data=None):
        url = f"{self.base_url}{path}"
        resp = self.session.put(url, json=json_data, timeout=TIMEOUT)
        return resp

    def delete(self, path):
        url = f"{self.base_url}{path}"
        resp = self.session.delete(url, timeout=TIMEOUT)
        return resp

    # 用户相关接口
    def get_users(self):
        return self.get("/users")

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")

    def create_user(self, data):
        return self.post("/users", json_data=data)

    # 帖子相关接口
    def get_posts(self):
        return self.get("/posts")

    def get_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def create_post(self, data):
        return self.post("/posts", json_data=data)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")
