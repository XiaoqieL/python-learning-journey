# ============ 第二十七天：爬虫基础 ============

import requests
from bs4 import BeautifulSoup
import re

# ====== 1. 最简单的爬虫：获取网页内容 ======
print("====1. 发送HTTP请求=====")

try:
    # 请求网页(headers模拟浏览器，防止被反爬)
    headers = {
        "User-Agent": "Mozila/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    resp = requests.get("http://httpbin.org/html", headers=headers, timeout=10)

    print(f"状态码：{resp.status_code}")
    print(f"响应长度：{len(resp.text)}字符")
    print(f"编码：{resp.encoding}")

    # 前200个字符预览
    print(f"\n内容预览：\n{resp.text[:200]}...")

    # ===== 2. 用BeautifulSoup解析网页HTML =====
    print("====2. 用BeautifulSoup解析网页HTML=====")

    soup = BeautifulSoup(resp.text, "lxml")

    # 获取标题
    title = soup.find("h1")
    if title:
        print(f"标题：{title.get_text().strip()}")

    # 获取所有段落
    paragraphs = soup.find_all("p")
    print(f"段落数：{len(paragraphs)}")
    for i, p in enumerate(paragraphs[:3]):  # 只显示前3段
        print(f"  段落{i + 1}:{p.get_text().strip()[:50]}...")

except Exception as e:
    print(f"网络请求失败：{e}")
    print("没关系，继续看本地HTML解析的例子！")

    # ====== 网络不通时用本地HTML练习 ======
    sample_html = """
    <html>
      <head><title>测试页面</title></head>
      <body>
        <h1>换欢迎来到爬虫入门</h1>
        <div class="news>
          <h2>新闻列表</h2>
          <ul>
            <li><a href="/news/1">第一条新闻</a><span>2026-7-30</span></li>
            <li><a href="/news/1">第二条新闻</a><span>2026-7-29</span></li>
            <li><a href="/news/1">第三条新闻</a><span>2026-7-28</span></li>
          </ul>
        </div>
        <div class="product>
          <h2>产品列表</h2>
          <div class="item"><h3>手机</h3><p class="price">￥2999</p></div>
          <div class="item"><h3>电脑</h3><p class="price">￥5999</p></div>
          <div class="item"><h3>耳机</h3><p class="price">￥599</p></div>
        </div>
      </body>
    </html>   
    """

    soup = BeautifulSoup(sample_html, "lxml")


    # 找标题
    print(f"标题：{soup.title.get_text()}")
    print(f"h1: {soup.find('h1').get_text()}")

    # 找到所有新闻标题 + 链接 + 日期
    print("\n===== 解析新闻列表=====")
    new_list = soup.select(".new li")  # CSS选择器
    for i in new_list:
        a_tag = li.find("a")
        date = li.find("span").get_text()
        print(f"   标题：{a_tag.get_text()}, 链接：{a_tag['href']}, 日期：{date}")

    # 找产品和价格
    print("\n===== 解析产品列表=====")
    prouduct = soup.select(".product .item")
    total_price = 0
    for p in prouduct:
        name = p.find("h3").get_text()
        price_text = p.select_one(".price").get_text()
        price_num = int(re.sub(r"\D", "", price_text)) # 提取数字
        total_price += price_num
        print(f"   {name}: {price_text} (数值：{price_num})")

    print(f"\n产品总价：¥{total_price}")

# ========== 3. 爬虫的几个基本步骤 ==========
print("====3. 爬虫的核心流程=====")
print("""
1. 请求网页：requests.get(url, headers=...)
2. 解析HTML：BeautifulSoup(html, "lxml")
3. 提取数据：find() / find_all() / select()
4. 保存数据：JSON / CSV / 数据库
""")

print("=" * 30)
print("第27天打卡完成！")
