# ============ 第二十二天：第3-4月阶段核心复习 ============

# 1. 装饰器
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[{func.__name__}] 耗时：{time.time() - start:.4f}秒")
        return result

    return wrapper


@timer
def my_func():
    total = sum(range(1000000))
    return total


print(f"结果：{my_func()}")


# 2. 生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b


print(f"斐波那契：{list(fib(10))}")

# 3. 上下文管理器
from contextlib import contextmanager


@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")


with tag("div"):
    print("  内容")

# 4. 标准库速览
from pathlib import Path
from datetime import datetime
import json

print(f"当前py文件数：{len(list(Path('.').glob('*.py')))}")
print(f"今天：{datetime.now().strftime('%Y-%m-%d')}")
print(f"JSON:{json.dumps({'day': 22, 'status': '打卡'})}")

# 5. pytest 速写
# assert 1 + 1 == 2
# pytest.raises(VaalueError)

# 6. 模块导入
import sys, threading

print(f"线程数：{threading.active_count()}")
print(f"Python版本：{sys.version.split()[0]}")

print("=" * 30)
print("第22天打卡完成！第3-4月阶段结束！")
