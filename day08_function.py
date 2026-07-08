# ============ 第八天：函数基础 ============

# 1. 最简单的函数
def say_hello():
    print("Hello!")
    print("今天第8天了")


# 2. 调用函数
say_hello()


# 2. 带参数的函数
def greet(name):
    print(f"你好，{name}!")


greet("小杰")
greet("Python")


# 3. 带返回值的函数
def add(a, b):
    return a + b


result = add(3, 5)
print(f"3+5 = {result}")


# 4. 默认参数
def power(base, exp=2):
    return base ** exp


print(f"3的平方：{power(3)}")
print(f"2的10次方：{power(2, 10)}")


# 5. 实战小函数：判断奇偶
def is_odd(num):
    return num % 2 != 0


for i in range(1, 11):
    if is_odd(i):
        print(f"{i}是奇数", end="")
print()

# 8. 第八天打卡
print('=' * 30)
print("第8天打卡完成！")
