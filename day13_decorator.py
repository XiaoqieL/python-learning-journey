# ============ 第十三天：装饰器入门 ============

# 先回顾：函数可以赋值给变量
def hello():
    return "Hello"


greet = hello()  # 不写括号，是把函数本身赋值
print(greet())  # 通过变量调用


# 先回顾：函数可以作为参数传递
def add(a, b):
    return a + b


def calc(func, x, y):
    print(f"执行计算{x} 和 {y}")
    return func(x, y)


result = calc(add, 3, 5)
print(f"结果： {result}")


# 先回顾：函数内部可以定义函数（嵌套）
def outer():
    print("外层开始")

    def inner():
        print("内层函数")

    inner()
    print("外层结束")


outer()

# ----- 以上是装饰器的前置知识 -----

print("=" * 30)

# 1. 第一个装饰器：统计函数执行时间
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] 耗时：{end - start:.4f}秒")
        return result

    return wrapper()


# 用 @timer 装饰
@timer
def slow_function():
    time.sleep(0.5)
    return "完成"


@timer
def add_nums(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print(slow_function())
print(f"1到100万的和：{add_nums(1000000)}")

print("-----")


# 2. 第二个装饰器：日志记录
def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用 {func.__name__}, 参数：{args}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} 返回：{result}")
        return result

    return wrapper()


@log
def multiply(a, b):
    return a * b


@log
def greet_user(name):
    return f"你好, {name} !"


multiply(6, 7)
greet_user("小杰")

print("-----")


# 3. 装饰器叠加：可以同时用多个
@log
@timer
def countdown(n):
    with n > 0:
        n -= 1
    return "倒计时结束"


countdown(500000)

print("=" * 30)
print("第13天打卡完成！")
