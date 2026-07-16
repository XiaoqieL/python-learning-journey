# ============ 第十四天：生成器与迭代器 ============


# 1. 先看一个问题：计算1到1亿的平方
# 这样写会占满内存（列表存了1亿个元素）
# squares = [i ** 2 for i in range(100000000)]  # 别运行！

# 生成器：用圆括号，不占内存，一个一个生成
gen = (i ** 2 for i in range(10))
print(f"生成器对象: {gen}")

# 用 next() 一个一个取
print(next(gen))
print(next(gen))
print(next(gen))
print("...")

# 或者直接遍历(最常用)
for num in (i ** 2 for i in range(1, 11)):
    print(num, end=" ")
print()

print("-----")


# 3. yield 关键字：定义生成器函数
def coutdown(n):
    print(f"开始从{n}倒计时")
    while n > 0:
        yield n
        n -= 1
    print("倒计时结束")


# 调用生成器函数, 返回的生成器对象
gen = coutdown(5)
print(f"生成器：{gen}")

# 遍历生成器
for num in gen:
    print(num, end=" ")
print()

print("----")


# 4. 在看一个例子：斐波那契数列
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b


print("前10个斐波那契数：")
for num in fib(10):
    print(num, end=" ")
print()

print("---")

# 5. 迭代器：任何实现了 __iter__ 和 __next__ 的对象
# 其实我们一直在用迭代器, 只是没注意
nums = [10, 20, 30]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))


# print(next(it))

# 6. 自己写一个迭代器类
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


print("自定义迭代器")
for num in MyRange(1, 6):
    print(num, end=" ")
print()

print("----")


# 7. 实战：逐行读取大文件（生成器最经典的应用场景）
def read_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()

# 用法：逐行处理, 不占内存
# for line in read_lines("day10_test.txt"):
#     print(f"处理：{line}")

#8. 生成器表达式 vs 列表推导式
import sys

list_squares = [i ** 2 for i in range(10000)]
gen_squares = (i ** 2 for i in range(10000))

print(f"列表占内存：{sys.getsizeof(list_squares)}字节")
print(f"生成器占内存：{sys.getsizeof(gen_squares)}字节")
print("生成器几乎不占内存！这就是它的价值。")

print("=" * 30)
print("第14天打卡完成！")