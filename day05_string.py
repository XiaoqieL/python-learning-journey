# ============ 第五天：字符串全套操作 ============

# 1. 字符串创建
s1 = "Hello, Python"
s2 = '你好世界'
s3 = """
这是多行字符串"""

print(s1)
print(s2)
print(s3)

# 2. 字符串拼接与重复
first = "Hello"
second = "World"
print(first + " " + second)
print("哈" * 3)

# 3. 字符串索引和切片
word = "Python"
print(f"第一个字符：{word[0]}")
print(f"最后一个：{word[-1]}")
print(f"前三个：{word[:3]}")
print(f"后三个：{word[-3:]}")
print(f"反转：{word[::-1]}")

# 4. 常用方法--大小写
name = "hello PYTHON"
print(name.upper())
print(name.lower())
print(name.title())
print("  hello  ".strip())

# 5. 常用方法---查找和替换
text = "Python is great, Python is easy"
print(f"出现次数：{text.count('Python')}")
print(f"第一次位置：{text.find('Python')}")
print(f"是否以P开头：{text.startswith('P')}")
print(f"是否以y结尾：{text.endswith('y')}")
print(text.replace("Python", "Py"))

# 6. 字符串分割和拼接
sentence = "我,是,软件,测试,工程师"
words = sentence.split(",")
print(f"分割结果：{words}")

joined = "-".join(words)
print(f"拼接结果：{joined}")

# 7. 判断方法
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())

# 8. 实战：统计一句话的单词数
msg = "Hello Python world"
print(f"单词数：{len(msg.split())}")

# 9. 实战：f-string 格式化
score = 90
name = "小杰"
print(f"{name}的成绩是{score}分, {'优秀' if score >= 90 else '继续努力'}")

# 10. 第五天打卡
print("=" * 30)
print("第5天打卡完成！")

