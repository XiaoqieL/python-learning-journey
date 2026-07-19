# ============ 第十五天：Python标准库高频模块 ============

import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
import json
import re
import logging

# ==== 1. os:操作系统接口=====
print("====os 模块 ====")
print(f"当前目录：{os.getcwd()}")
print(f"目录分隔符：{os.sep}")
print(f"环境变量PATH：{os.environ.get('PATH', '')[:50]}...")

# 遍历目录
print("\n当前目录下的文件：")
for item in os.listdir("."):
    if item.endswith(".py"):
        print(f"  {item}")

# ===== 2. pathlib：面向对象的路径处理（推荐！比os好用）=====
print("\n====== pathlib模块 =====")
p = Path(".")
print(f" 当前路径：{p.absolute()}")
print(f"是否是目录：{p.is_dir()}")

# 查找所有py文件
py_files = list(p.glob("*.py"))
print(f"找到 {len(py_files)} 个py文件")

# 路径拼接
new_path = p / "data" / "test.txt" # / 拼接路径,跨平台
print(f"拼接路径：{new_path}")

# ===== 3. datetime: 日期时间处理 =====
print("\n===== datetime 模块 =====")
now = datetime.now()
print(f"当前时间：{now}")
print(f"格式化：{now.strftime('%Y-%m-%d %H:%H:%S')}")
print(f"年：{now.year} 月：{now.month} 日：{now.day}")

# 日期运算
tomorrow = now + timedelta(days=1)
print(f"明天：{tomorrow.strftime('%Y-%m-%d')}")

last_week = now - timedelta(weeks=1)
print(f"一周前：{last_week.strftime('%Y-%m-%d')}")

# 字符串转日期
date_str = "2026-07-19"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print(f"解析后的日期：{parsed}")

# ===== 4. json: JSON处理 =====
print("\n===== json 模块 =====")

# Python对象 -> JSON字符串
student = {
    "name": "小杰",
    "age": 28,
    "scores": [92, 85, 78],
    "pass": True
}
json_str = json.dumps(student, ensure_ascii=False, indent=2)
print(f"Json: \n{json_str}")

# JSON字符串 -> Python对象
back = json.loads(json_str)
print(f"解析后：name={back['name']}, scores={back['scores']}")

# 写入JSON文件
with open("day16_data.json", "w", encoding="utf-8") as f:
    json.dump(student, f, ensure_ascii=False, indent=2)
print("JSON文件已保存")

# 读取JSON文件
with open("day16_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(f"从文件读取：{data['name']}")

# ===== 5. re: 正则表达式 =====
print("\n===== re 模块 =====")

text = "我的手机号是13812345678, 邮箱是xiaojie@test.com, QQ是123456789"

# 查找手机号
phones = re.findall(r"1[3-9]\d{9}", text)
print(f"手机号：{phones}")

# 查找邮箱
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(f"邮箱：{emails}")

# 替换铭感信息
masked = re.sub(r"1[3-9]\d{9}", "***", text)
print(f"脱敏后：{masked}")

# 验证是否匹配
is_valid_email = bool(re.match(r"^[\w.-]+@[\w.-]+\.\w+$","test@example.com"))
print(f"test@example.com 是有效邮箱：{is_valid_email}")

# ===== 6. logging: 日志处理 =====
print("\n===== logging 模块 =====")

# 基础配置（只需配置一次）
logging.basicConfig(
    level=logging.DEBUG,
    format="%(acstime)s - %(levelname)s - %(messages)",
    datefmt="%H:%H:%S"
)

logging.debug("这是调试信息")
logging.info("这是普通信息")
logging.warning("这是警告")
logging.error("这是错误")
logging.critical("这是严重错误")

print("=" * 30)
print("第16天打卡完成！")