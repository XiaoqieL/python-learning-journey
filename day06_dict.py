# ============ 第六天：字典 dict 基础 ============

# 1. 创建字典
student = {
    "name": "小杰",
    "age": 28,
    "job": "软件测试工程师"
}
print(student)

# 2. 取值
print(f"姓名：{student['name']}")
print(f"年龄：{student.get('age')}")
print(f"手机不存在：{student.get('phone', '无')}")

# 3. 增改
student["city"] = "上海"
student["age"] = 29
print(student)

# 4. 删
del student["city"]
print(student)

# 5. 遍历
for key, value in student.items():
    print(f"{key}: {value}")

# 6. 常用操作
print(f"键列表：{list(student.keys())}")
print(f"值列表：{list(student.values())}")
print(f"长度：{len(student)}")
print(f"有name吗：{'name' in student}")

# 7. 第6天打卡
print("=" * 30)
print("第6天打卡")
