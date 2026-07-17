# ============ 第十五天：上下文管理器 ============


# 1. 为什么需要上下文管理器？
# 不用 with 的写法：要手动关闭,容易忘
f = open("day15_test.txt", "w", encoding="utf-8")
f.write("Hello\n")
f.close()

# 2. 用with 的写法：自动关闭
with open("day15_test.txt", "w", encoding="utf-8") as f:
    f.write("用with更安全\n")
    f.write("就算中间报错也会自动关闭\n")


# 出了with块, f自动关闭了，不用手动调用close()

# 3. 自己写一个上下文管理器---用类
class MyTimer:
    def __enter__(self):
        import time
        self.start = time.time()
        print("开始计时...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.time() - self.start
        print(f"结束计时, 耗时：{elapsed:.4f}秒")
        return True


# 使用
with MyTimer():
    total = 0
    for i in range(1000000):
        total += i
    print(f"总和：{total}")

# 4. 更简单的写法 --- 用@contextmanager装饰器
from contextlib import contextmanager


@contextmanager
def my_open(filename, mode="r", encoding="utf-8"):
    f = open(filename, mode, encoding=encoding)
    try:
        yield f
    finally:
        f.close()
        print("文件已关闭")


# 使用
with my_open("day_15_test.txt", "r") as f:
    content = f.read()
    print(f"读取内容：{content[:30]}...")

# 5. 在一个实战：零时切换工作目录
import os


@contextmanager
def temp_chdir(path):
    old_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_path)


print(f"当前目录：{os.getcwd()}")
# with temp_chdir("D:\\"):
#     print(f"临时目录: {os.getcwd()}")
# print(f"恢复: {os.getcwd()}")

print("=" * 30)
print("第15天打卡完成！")
