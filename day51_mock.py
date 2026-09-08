# ============ 第五十一天：Mock模拟测试 ============

from unittest.mock import Mock, patch, MagicMock

# ============================================================
# 一、Mock 基础：创建一个假对象
# ============================================================
print("=" * 50)
print("  一、Mock 基础")
print("=" * 50)

mock = Mock()
mock.say_hello_value = "你好，我是Mock!"  # 预设返回值
mock.add.return_value = 30  # 预设返回值

# 调用 Mock 的方法，返回预设值
print(f"mock.say_here(): {mock.say_hello()}")
print(f"mock.add(1, 2): {mock.add(1, 2)}")  # 返回30，忽略参数

# 模拟异常
mock.get_data.side_effect = ConnectionError("数据库连接失败")
try:
    mock.get_data()
except ConnectionError as e:
    print(f"mock.get_data() 抛出异常：{e}")

# ============================================================
# 二、实际场景：测试依赖外部数据库的函数
# ============================================================
print(f"\n{'=' * 50}")
print("  二、测试真实场景")
print("=" * 50)


# 我们要测试的代码(假设它依赖数据库查询)
def calculate_total_order(order_id):
    """从数据库拿订单金额，计算含税总价"""
    amount = get_order_amount(order_id)  # 这个函数访问数据库！
    tax = amount * 0.1
    return amount + tax


# 真实的数据库查询函数(我们不想真的执行)
def get_order_amount(order_id):
    # 真实逻辑：查询数据库，这里跳过
    raise NotImplementedError("真实环境才执行数据库查询")


# --- 用 patch 替换 get_order_amount ---
@patch("__main__.get_order_amount")  # 把函数替换成Mock
def test_with_mock(mock_get_amount):
    mock_get_amount.return_value = 100  # 假装数据库返回 100

    result = calculate_total_order("ORD-001")
    return result


# 运行测试，不用真实数据库
result = test_with_mock()
print(f"含税总价：{result}")  # 100 + 10 = 110
print("→ 用Mock模拟数据库返回100，成功测出含税逻辑！")

# ============================================================
# 三、用 Mock 测第三方API调用
# ============================================================
print(f"\n{'=' * 50}")
print("  三、测试第三方API调用")
print("=" * 50)


class WeatherService:
    """依赖第三方天气API的服务"""

    def __init__(self, api_client):
        self.api_client = api_client

    def get_weather_report(self, city):
        """调用API获取天气并格式化"""
        # 这里会真的发HTTP请求！
        data = self.api_client.fetch_weather(city)
        return f"{city}的天气是{data['weather']}，温度是{data['temperature']}°C"


# --- 用手动Mock替代真实的api_client ---
def test_weather():
    # 创建一个假的客户端
    fake_client = Mock()
    # 预设返回数据
    fake_client.fetch_weather.return_value = {
        "status": "晴",
        "temperature": 25
    }

    service = WeatherService(fake_client)  # 注入假客户端
    report = service.get_weather_report("北京")

    print(f"报告: {report}")
    print(f"→ 没有真的调用API，纯测试了格式化逻辑")
    print(f"→ 验证: fetch_weather 被调用了 {fake_client.fetch_weather.call_count} 次")
    print(f"→ 参数是: {fake_client.fetch_weather.call_args}")

    return report


# 注意：测试函数名以test_开头，但这里直接调用演示
test_weather()

# ============================================================
# 四、assert_called_with：验证调用参数
# ============================================================
print(f"\n{'=' * 50}")
print("  四、验证Mock被正确调用")
print("=" * 50)

mock_api = Mock()
mock_api.send_data(age=28, name="小杰")

# 验证：是否用正确的参数调用了send_data
mock_api.send_data.assert_called_with(age=28, name="小杰")
print("✓ send_data 被用正确的参数调用 (age=28, name=小杰)")

# 验证是否被调用过
mock_api.send_data.assert_called()
print("✓ send_data 确实被调用过")

# assert_called_with 用错参数会抛异常
try:
    mock_api.send_data.assert_called_with(age=28, name="错误")
except AttributeError as e:
    print(f"✗ 用错误参数验证时抛异常: {e}")

# ============================================================
# 五、MagicMock：自动支持魔术方法
# ============================================================
print(f"\n{'=' * 50}")
print("  五、MagicMock 和 Mock 的区别")
print("=" * 50)

# Mock 不支持 len() 等魔术方法
# m = Mock()
# len(m)  # 报错！

mm = MagicMock()   # MagicMock 自动支持魔术方法
mm.__len__.return_value = 7
print(f"len(MagicMock): {len(mm)}")  # 7

# 对比: 普通
print("""
对比总结：
   Mock        → 用于普通方法
  MagicMock   → 额外支持魔术方法（__len__/__iter__等）
  patch       → 临时替换类或函数（with或装饰器）
  return_value    → 预设返回值
  side_effect     → 预设异常或依次返回值
  assert_called_with → 验证调用参数
  call_count       → 查看调用次数
""")

print("第51天打卡完成！Mock测试入门！")
