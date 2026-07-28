# ============ 第二十五天：网络协议基础 ============

import socket
import urllib.request
import json

# ===== 1. 网络分层（简单理解）====
print("====网络分层====")

# 生活中寄快递的类比：
# 应用层（HTTP/HTTPS）→ 你写的信件内容
# 传输层（TCP/UDP）→ 快递公司选顺丰还是普通
# 网络层（IP）→ 收获地址
# 数据链路层（MAC）→ 具体送货路线

print("HTTP = 应用层协议（浏览网页、API接口）")
print("TCP = 传输层(可靠传输，三次握手)")
print("UDP = 传输层(快速传输，不保证到达)")
print("IP = 网络层协议（找地址,192.168.1.1）")

# ===== 2. 端口和IP =====
print("\n====IP和端口 =====")

# IP地址 = 电脑地址
# 端口 = 程序的"门牌号"
# 一个电脑有65535个端口
# 80 = HTTP默认端口
# 443 = HTTPS默认端口
# 3306 = MySQL默认端口
# 22 = SSH默认端口

print(f"本机IP:{socket.gethostbyname(socket.gethostname())}")
print(f"常用端口：80（HTTP）443（HTTPS）3306(MySQL) 22(SSH)")

# ===== 3. HTTP请求（Python发网络请求）=====
print("\n==== HTTP请求====")

# GET请求：获取数据
try:
    response = urllib.request.urlopen("https://httpbin.org/get", timeout=10)
    data = json.loads(response.read().decode())
    print(f"状态码：{response.status}")
    print(f"我的IP（服务器看到的）：{data.get('origin', '未知')}")
    print(f"请求头：{list(data.get('headers', {}).keys())}")
except Exception as e:
    print(f"网络请求失败：{e}")
    print("(网络问题不影响学习,理解代码逻辑就行)")

# ===== 4. HTTP状态码(必记)=====
print("\n====HTTP状态码=====")

status_codes = {
    200: "OK - 请求成功",
    201: "Created - 创建成功",
    301: "Move Permanently - 永久重定向",
    302: "Found - 零时重定向",
    400: "Bad Request - 参数错误",
    401: "Unauthorized - 未登录",
    403: "Forbidden - 无权限",
    404: "Not Found - 资源不存在",
    500: "Internal Server Error - 服务器内部错误",
    502: "Bad Gateway - 网关错误",
    503: "Service Unavailable - 服务不可用",
}

for code, desc in status_codes.items():
    print(f"     {code}: {desc}")

# ======5. TCP vs UDP ======
print("\n===== TCP VS UDP=====")

print("""
TCP(可靠):
  - 三次握手建立连接
  - 保证数据不丢、不乱、不重复
  - 网页、文件传输、邮件都用TCP
  - 速度慢一点但可靠
  
UDP(快速)：
  - 不建立连接，直接发
  - 不保证到达，可能丢包
  - 视频直播、游戏、DNS查询用UDP
  - 速度但不可靠
""")

# ===== 6. Socket编程（最底层的网络通信）=====
print("====== Socket基础（了解）=====")

# TCP服务端示例（不运行，只看结构）
server_code = """
import socket

# 创建TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8888))   # 绑定IP和端口
server.listen(5)                  # 开始监听

print("服务端启动，等待连接...")
client, addr = server.accept()    # 接受客户端连接
data = client.recv(1024)          # 接收数据
client.send(b"Hello from server") # 发送数据
client.close()
"""
print("TCP服务端核心步骤：socket → bind → listen → accept → recv/send")
print("TCP客户端核心步骤：socket → connect → send/recv")

print("\n" + "=" * 30)
print("第25天打卡完成！")


