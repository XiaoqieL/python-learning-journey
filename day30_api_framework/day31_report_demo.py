# ============ 第三十一天：pytest测试报告 ============

import pytest
import requests
import time


# ===== 1. 带标记的测试用例 =====

class TestAPIReport:
    """接口测试 - 带详细断言信息"""

    BASE_URL = "https://jsonplaceholder.typicode.com"

    @pytest.mark.smoke
    @pytest.mark.parametrize("endpoint, expected_count", [
        ("/users", 10),
        ("/posts", 100),
        ("/comments", 500)
    ])
    def test_data_count(self, endpoint, expected_count):
        """验证数据总量"""
        resp = requests.get(f"{self.BASE_URL}{endpoint}", timeout=30)
        assert resp.status_code == 200, f"接口{endpoint}返回{resp.status_code}"
        data = resp.json()
        assert len(data) == expected_count, \
            f"接口{endpoint}期望{expected_count}条,实际{len(data)}条"

    @pytest.mark.smoke
    def test_create_post(self):
        """验证创建帖子"""
        resp = requests.post(
            f"{self.BASE_URL}/posts",
            json={"title": "测试报告", "body": "第31天", "userId": 1},
            timeout=10
        )
        assert resp.status_code == 201
        result = resp.json()
        assert result["title"] == "测试报告"
        assert "id" in result, "返回数据缺少id字段"

    @pytest.mark.regression
    def test_response_time(self):
        """验证响应时间不超过3秒"""
        start = time.time()
        resp = requests.get(f"{self.BASE_URL}/users/1", timeout=30)
        elapsed = time.time() - start
        assert resp.status_code == 200
        assert elapsed < 3.0, f"响应时间{elapsed:.2f}秒,超过3秒阈值"

    @pytest.mark.regression
    def test_user_data_structure(self):
        """验证用户数据结构完整性"""
        resp = requests.get(f"{self.BASE_URL}/users/1", timeout=30)
        user = resp.json()
        required_fields = ["id", "name", "username", "email", "address", "phone"]
        for field in required_fields:
            assert field in user, f"用户数据缺少字段：{field}"
