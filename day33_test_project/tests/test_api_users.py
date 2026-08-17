import pytest


class TestAPIUsers:
    """用户接口测试"""

    def test_get_all_users(self, api):
        """获取所有用户"""
        resp = api.get("/users")
        assert resp.status_code == 200
        user = resp.json()
        assert len(user) == 10

    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
    def test_get_user_by_id(self, api, user_id):
        """根据ID获取用户"""
        resp = api.get(f"/users/{user_id}")
        assert resp.status_code == 200
        assert resp.json()["id"] == user_id

    def test_create_user_data_driven(self, api, user_data):
        """数据驱动：从CSV读取多组数据创建用户"""
        for user in user_data:
            resp = api.post("/users", json_data={
                "name": user["name"],
                "username": user["username"],
                "email": user["email"]
            })
            expected = int(user["expected_status"])
            assert resp.status_code == expected, \
                f"创建{user['name']}失败：期望{expected}, 实际{resp.status_code}"
            result = resp.json()
            assert result["name"] == user["name"]
            assert "id" in result

    def test_create_user_structure(self, api):
        """验证返回数据结构"""
        resp = api.post("/users", json_data={"name": "测试", "email": "t@t.com"})
        result = resp.json()
        required = ["id", "name", "email"]
        for field in required:
            assert field in result, f"缺少字段：{field}"

    def test_delete_user(self, api):
        """删除用户"""
        resp = api.delete("/users/1")
        assert resp.status_code == 200



