import pytest


class TestUIForm:
    """UI表单测试"""

    def test_login_form(self, browser_page):
        """测试登录表单"""
        html = """
        <html><body>
            <form id="login">
                <input id="user" type="text" placeholder="用户名" />
                <input id="pass" type="password" />
                <select id="role">
                    <option value="">请选择</option>
                    <option value="tester">测试</option>
                    <option value="dev">开发</option>
                </select>
                <input id="remember" type="checkbox" />
                <button type="submit" id="submit">登录</button>
            </form>
            <div id="msg" style="display:none">登录成功</div>
            <script>
                document.getElementById('login').addEventListener('submit', function(e) {
                    e.preventDefault();
                    var u = document.getElementById('user').value;
                    var p = document.getElementById('pass').value;
                    if (u && p) {
                        document.getElementById('msg').style.display = 'block';
                        document.getElementById('msg').textContent = '登录成功';
                    } else {
                        document.getElementById('msg').style.display = 'block';
                        document.getElementById('msg').textContent = '请填写完整';
                    }
                });
            </script>
        </body></html>
        """
        page = browser_page
        page.set_content(html)

        # 正常登录
        page.fill("#user", "admin")
        page.fill("#pass", "123456")
        page.select_option("#role", "tester")
        page.check("#remember")
        page.click("#submit")

        page.wait_for_selector("#msg:visible")
        msg = page.locator("#msg").text_content()
        assert msg == "登录成功"
        assert page.is_checked("#remember") == True

    def test_empty_form_validation(self, browser_page):
        """测试空表单验证"""
        html = """
        <html><body>
            <form id="login">
                <input id="user" type="text" />
                <input id="pass" type="password" />
                <button type="submit" id="submit">登录</button>
            </form>
            <div id="msg" style="display:none"></div>
            <script>
                document.getElementById('login').addEventListener('submit', function(e) {
                    e.preventDefault();
                    document.getElementById('msg').style.display = 'block';
                    document.getElementById('msg').textContent = '请填写完整';
                });
            </script>
        </body></html>        
        """

        page = browser_page
        page.set_content(html)

        # 不填直接提交
        page.click("#submit")
        page.wait_for_selector("#msg:visible")
        msg = page.locator("#msg").text_content()
        assert msg == "请填写完整"

    def test_screenshot(self, browser_page):
        """截图测试"""
        page = browser_page
        page.set_content("<html><body><h1>自动化测试截图</h1></body></html>")
        page.screenshot(path="day33_screenshot.png")
        assert page.locator("h1").text_content() == "自动化测试截图"
