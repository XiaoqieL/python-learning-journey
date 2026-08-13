# ============ 第三十二天：Playwright UI自动化入门 ============

from playwright.sync_api import sync_playwright
import pytest
import time


# ===== 1. 第一个UI自动化：打开网页截图 =====

def test_baidu_search():
    """搜索并截图"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.bing.com", wait_until="domcontentloaded")
        print(f"页面标题：{page.title()}")

        # 必应的搜索框
        page.locator("#sb_form_q").fill("Python自动化测试")
        page.locator("#search_icon").click()
        page.wait_for_timeout(3000)

        page.screenshot(path="day32_search.png")
        print("截图已保存")

        title = page.title()
        assert "Python" in title or "python" in title.lower()

        browser.close()


# ===== 2. 元素定位（核心！）=====

def test_locator_methods():
    """演示各种元素定位方式"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # 用本地HTML练习（不依赖网络）
        html = """
               <html>
               <body>
                   <input id="username" placeholder="请输入用户名" />
                   <input id="password" type="password" />
                   <button class="submit-btn">登录</button>
                   <button class="cancel-btn">取消</button>
                   <a href="/home">首页</a>
                   <div class="user-info">
                       <span class="name">小杰</span>
                       <span class="role">测试工程师</span>
                   </div>
                   <ul class="menu">
                       <li>首页</li>
                       <li>产品</li>
                       <li>关于</li>
                   </ul>
               </body>
               </html>
               """
        page.set_content(html)

        # 方式1：通过ID定位（最常用）
        username = page.locator("#username")
        print(f"用户名输入框placeholder: {username.get_attribute('placeholder')}")

        # 方式2：通过CSS选择器定位
        login_btn = page.locator(".submit-btn")
        print(f"登录按钮文字: {login_btn.text_content()}")

        # 方式3：通过文本定位（Playwright特色！）
        cancel_btn = page.locator("button:has-text('取消')")
        print(f"取消按钮: {cancel_btn.text_content()}")

        # 方式4：链式定位（先找父元素再找子元素）
        name = page.locator(".user-info .name")
        print(f"用户名: {name.text_content()}")

        # 方式5：定位多个元素
        menu_items = page.locator(".menu li")
        print(f"菜单项数量: {menu_items.count()}")
        for i in range(menu_items.count()):
            print(f"  菜单{i + 1}: {menu_items.nth(i).text_content()}")

        browser.close()


# ===== 3. 表单操作实战 =====

def test_form_operations():
    """表单填写和提交"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        html = """
        <html>
        <body>
             <form id="loginForm">
                 <input id="user" type="text" />
                 <input id="pass" type="password" />
                 <select id="role">
                    <option value="">请选择</option>
                    <option value="tester">测试工程师</option>
                    <option value="dev">开发工程师</option>
                 </select>
                 <input id="remember" type="checkbox" />
                 <label for="remember">记住我</label>
                 <button type="submit">登录</button>
             </form>
             <div id="result" style="display:none">登录成功</div>
             <script>
                  document.getElementById('loginForm').addEventListener('submit', function(e){
                      e.preventDefault();
                      document.getElementById('result').style.display = 'block';
                  });
             </script>
        </body>
        </html>       
        """

        page.set_content(html)

        # 填写表单
        page.fill("#user", "admin")
        page.fill("#pass", "123456")

        # 选择下拉框
        page.select_option("#role", "tester")

        # 选择复选框
        page.check("#remember")

        # 验证填写内容
        assert page.input_value("#user") == "admin"
        assert page.input_value("#pass") == "123456"
        assert page.input_value("#role") == "tester"
        assert page.is_checked("#remember") == True

        # 点击登录
        page.click("button[type='submit']")

        # 验证结果出现
        result = page.locator("#result")
        page.wait_for_selector("#result:visible")
        assert result.text_content() == "登录成功"
        print("表单测试通过！")

        browser.close()


# ===== 4. pytest + Playwright 结合 =====

@pytest.fixture
def page():
    """每个测试自动启动和关闭浏览器"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()


def test_page_title(page):
    """用fixture测试页面标题"""
    page.set_content("<html><head><title>测试页面</title></head><body>Hello</body></html>")
    assert page.title() == "测试页面"


def test_input_value(page):
    """用fixture测试输入框"""
    page.set_content('<input id="test" />')
    page.fill("#test", "Playwright真好用")
    assert page.input_value("#test") == "Playwright真好用"
