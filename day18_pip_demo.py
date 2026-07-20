# ============ 第18天：验证pip安装 ============

# 先在终端运行：pip install requests
import requests

try:
    r = requests.get("http://www.baidu.com", timeout=5)
    print(f"百度状态码：{r.status_code}")
    print(f"响应长度：{len(r.text)}")
    print("requests库安装成功，网络请求正常！")
except Exception as e:
    print(f"网络请求失败：{e}")
    print("但pip和虚拟环境的配置是对的，只是网络问题")

print("=" * 30)
print("第18天打卡完成！")