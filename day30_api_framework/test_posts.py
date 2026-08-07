import pytest

class TestPosts:

    def test_get_all_posts(self, api):
        resp = api.get_posts()
        assert resp.status_code == 200
        posts = resp.json()
        assert len(posts) == 100

    @pytest.mark.parametrize("post_id", [1, 50, 100])
    def test_get_post(self, api, post_id):
        resp = api.get_post(post_id)
        assert resp.status_code == 200
        post = resp.json()
        assert post["id"] == post_id
        assert "title" in post
        assert "body" in post

    def test_create_post(self, api):
        post_data = {
            "title": "Python测试",
            "body": "今天学了接口自动化",
            "userId": 1
        }
        resp = api.create_post(post_data)
        assert resp.status_code == 201
        result = resp.json()
        assert result["title"] == "Python测试"

    def test_delete_post(self, api):
        resp = api.delete_post(1)
        assert resp.status_code == 200

    def test_post_response_time(self, api):
        """测试响应时间"""
        import time
        start = time.time()
        resp = api.get_posts()
        elapsed = time.time() - start
        assert resp.status_code == 200
        assert elapsed < 5.0, f"响应太慢：{elapsed:.2f}秒"
