# ============ 第四天：for循环和while循环 ============

# 1. for 循环---打印1到5
for i in range(1, 6):
    print(i)

# 2. for循环---1到100求和
total = 0
for i in range(1, 101):
    total += i
print(f"1到100的和：{total}")

# 3. for 循环--遍历列表
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# 4. while 循环--倒计时
count = 5
while count > 0:
    print(f"倒计时：{count}")
    count -= 1
print("发射！")

# 5. 循环控制 ----break 和 continue
# break：找到就停
for i in range(1, 11):
    if i == 7:
        break
    print(i, end="")
print("\n---")

# continue:跳过偶数，只打印奇数
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end="")
print("\n---")

# 6. 嵌套循环--九九乘法表(直到5)
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}", end="\t")
    print()

# 7. 第四天打卡
print("=" * 30)
print("第四天打卡完成！")
