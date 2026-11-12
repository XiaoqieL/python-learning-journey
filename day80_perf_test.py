import logging
import os
import time

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "perf.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=LOG_FILE,
    filemode="a",
)

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        cost = time.time() - self.start
        logging.info(f"耗时 {cost:.4f} 秒")
        return False


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        cost = time.time() - start
        logging.info(f"{func.__name__} 耗时 {cost:.4f} 秒")
        return result

    return wrapper


@timing
def test_loop_decorator():
    """用装饰器测 100 万次循环"""
    i = 0
    for i in range(1000000):
        i += 1


def test_loop_context():
    """用 with Timer 测同样的循环"""
    with Timer():
        y = 0
        for y in range(1000000):
            y += 1


test_loop_decorator()
test_loop_context()
