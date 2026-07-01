# ============ 第二天：运算符 + if 判断 ============

# 1. 算数运算符
a = 10
b = 3
print(f"加法：{a + b}")
print(f"减法：{a - b}")
print(f"乘法：{a * b}")
print(f"除法：{a / b}")
print(f"整除：{a // b}")
print(f"取余：{a % b}")
print(f"幂：{a ** b}")

# 2. 比较运算符
print(f"10 == 3:{a == b}")
print(f"10 != 3:{a != b}")
print(f"10 > 3:{a > b}")

# 3. if 判断--成绩等级
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"成绩：{score},等级：{grade}")

# 4.简单逻辑判断
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("可以入场")
else:
    print("不可以入场")

# 5. 第二天打卡
print("=" * 30)
print("第2天打卡完成！")
