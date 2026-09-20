# ============ 猜数字游戏 ============
import random

target = random.randint(1, 100)
guess = 0
attempts = 0

print("我已经想好了一个 1~100 之间的数，你来猜：")

while guess != target:
    guess = int(input("请输入你的猜测："))  # 没猜中就不断循环
    attempts += 1

    if guess < target:
        print("太小了，再大点！")
    elif guess > target:
        print("太大了，再小点！")
    else:
        print(f"恭喜你，猜对了！答案是 {target}，你一共猜了 {attempts} 次。")

print("游戏结束！")
