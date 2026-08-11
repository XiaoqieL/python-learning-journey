import pytest


class TestUsers:

    def test_get_all_user(self, api):
        """测试获取所有用户"""
        resp = api.get_users()
        assert resp.status_code == 200
        users = resp.json()
        assert len(users) > 0
        assert isinstance(users, list)

    @pytest.mark.parametrize("user_id, expected_name", [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch"),
    ])
    def test_get_user_by_id(self, api, user_id, expected_name):
        """参数化测试：根据ID获取用户"""
        resp = api.get_user(user_id)
        assert resp.status_code == 200
        user = resp.json()
        assert user["id"] == user_id
        assert user["name"] == expected_name

    def test_get_nonexist_user(self, api):
        """测试获取不存在的用户（返回404）"""
        resp = api.get_user(99999)
        assert resp.status_code == 404

    def test_create_user(self, api, new_user_data):
        """测试创建用户"""
        resp = api.create_user(new_user_data)
        assert resp.status_code == 201
        result = resp.json()
        assert result["name"] == new_user_data["name"]
        assert result["email"] == new_user_data["email"]
        assert "id" in result

    def test_user_has_email(self, api):
        """测试用户数据结构：每个用户必须有email"""
        resp = api.get_users()
        users = resp.json()
        for user in users:
            assert "email" in user, f"用户{user.get('id')}没有email"
            assert "@" in user["email"], f"用户{user['id']}的email格式错误"
