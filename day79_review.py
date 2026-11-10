import time


class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        cost = time.time() - self.start
        print(f"耗时 {cost:.4f} 秒")
        return False


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        cost = time.time() - start
        print(f"{func.__name__} 耗时 {cost:.4f} 秒")
        return result

    return wrapper


def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        print(count)

    return inc


with Timer():
    time.sleep(1)


@timing
def slow():
    time.sleep(0.5)


slow()

c1 = counter()
c2 = counter()
c1()  # 1
c1()  # 2
c2()  # 1（c2 自己的，不跟 c1 混）
c1()  # 3

def test_try_flow():
    """验证 try/except/else/finally 的执行路径"""
    print("===测试1：成功路径 ===")
    try:
        x = 10 / 2
        print("try: 计算成功")
    except ZeroDivisionError:
        print("except: 出错了")
    else:
        print("else: 只有成功才执行，结果是", x )
    finally:
        print("finally: 无论如何都执行")

    print("\n=== 测试2：失败路径 ===")
    try:
        y = 10 / 0
        print("try: 计算成功")
    except ZeroDivisionError:
        print("except: 出错了, 被接住")
    else:
        print("else:只有成功才执行")
    finally:
        print("finally: 无论如何都执行")

test_try_flow()