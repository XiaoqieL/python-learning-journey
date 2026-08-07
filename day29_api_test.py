# ============ 第二十九天：requests接口测试入门 ============
# 接口测试 = 测试后端API，不测界面，只测数据对不对

import requests
import json

# ===== 1. GET请求：获取数据 =====
print("=====GET请求======")
try:
    resp = requests.get("https://httpbin.org/get", params={"name": "小杰", "age": 28}, timeout=10)
    print(f"状态码：{resp.status_code}")
    print(f"响应JSON：{resp.json()}")
except Exception as e:
    print(f"网络不通：{e}")


# ===== 2. POST请求：提交数据 =====
print("\n=====POST请求====")
try:
    data = {"username": "admin", "password": "123456"}
    resp = requests.post("https://httpbin.org/post", json=data, timeout=10)
    print(f"状态码：{resp.status_code}")
    result = resp.json()
    print(f"服务端端收到：{result.get('json', {})}")
except Exception as e:
    print(f"网络不通：{e}")

# ===== 3. requests核心属性（记住这5个）=====
print("\n==== 核心属性 =====")
try:
    resp = requests.get("https://httpbin.org/get", timeout=10)
    print(f"resp.status_code  → 状态码: {resp.status_code}")
    print(f"resp.text         → 文本：{resp.text[:50]}...")
    print(f"resp.json()       → JSON：{type(resp.json())}")
    print(f"resp.headers      → 响应头：{dict(list(resp.headers.items())[:3])}")
    print(f"resp.url          → 实际URL：{resp.url}")
except Exception as e:
    print(f"网络不通，理解代码即可：{e}")

# ===== 4. 写一个接口测试函数（测试工程师日常）=====
print("\n==== 接口测试函数示例 ====")


def test_api(url, method="GET", params=None, json_data=None, expected_code=200):
    """通用接口测试函数"""
    try:
        if method == "GET":
            resp = requests.get(url, params=params, timeout=10)
        elif method == "POST":
            resp = requests.post(url, json=json_data, timeout=10)
        else:
            return False, f"不支持方法：{method}"

        # 断言状态码
        if resp.status_code == expected_code:
            return True, f"PASS - 状态码{resp.status_code}"
        else:
            return False, f"FAIL - 期望{expected_code}, 实际{resp.status_code}"
    except Exception as e:
        return False, f"ERROR - {e}"


# 测试用例
test_cases = [
    ("GET接口测试", "https://httpbin.org/get", "GET", {"q": "test"}, None, 200),
    ("POST接口测试", "https://httpbin.org/post", "POST", None, {"name": "test"}, 200),
    ("404测试", "https://httpbin.org/notexist", "GET", None, None, 404),
]

print(f"{'用例名':<16} {'结果':<8} {'详情'}")
print("-" * 50)
for name, url, method, params, data, code in test_cases:
    passed, msg = test_api(url, method, params, data, code)
    status = "✓ PASS" if passed else "✗ FAIL"
    print(f"{name:<16} {status:<8} {msg}")

print("\n" + "=" * 30)
print("第29天打卡完成！接口测试入门！")
