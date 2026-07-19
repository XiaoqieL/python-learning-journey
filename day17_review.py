# ============ 第十七天：复习前16天核心知识点 ============

# 1. 变量和类型
name = "小茄"
age = 28
score = 92.5
passed = True
print(f"姓名:{name} 年龄：{age} 分数：{score} 通过：{passed}")

# 2. if判断
if score >= 90:
    grade = "优秀"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"等级：{grade}")

# 3. 循环
total = 0
for i in range(1, 100):
    total += i
print(f"1到100和：{total}")

# 4. 四大容器
my_list = [1, 2, 3, 3, 5]  # 列表：可改，有顺序
my_dict = {"a": 1, "b": 2, "c": 3}  # 字典：键值对
my_tuple = (1, 2, 3)  # 元组：不可改
my_set = {1, 2, 3, 3}  # 集合：自动去重
print(f"list:{my_list} dict:{my_dict} tuple:{my_tuple} set:{my_set}")


# 5. 函数
def add(a, b):
    return a + b


print(f"3+5={add(3, 5)}")

#6. 文件读写
with open("day17_review.txt", "w", encoding="utf-8") as f:
    f.write("复习完毕，好好休息把！\n")
print("文件已写入")

# 7. 第17天打卡
print("=" * 30)
print("第17天打卡完成！好好休息！")