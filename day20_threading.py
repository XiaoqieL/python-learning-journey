# ============ 第二十天：多线程和多进程基础 ============

import time
import threading
from concurrent.futures import ThreadPoolExecutor


# 1. 先看：不使用多线程，顺序执行需要多久
def task(name, seconds):
    print(f"[任务{name}] 开始,需要{seconds}秒")
    time.sleep(seconds)
    print(f"[任务{name}] 完成")


print("====不使用多线程（顺序执行）====")
start = time.time()
task("A", 2)
task("B", 2)
print(f"总耗时：{time.time() - start:.1f}秒")

print("\n===== 使用多线程（并行执行）")
start = time.time()

# 创建两个线程
t1 = threading.Thread(target=task, args=("A", 2))
t2 = threading.Thread(target=task, args=("B", 2))

# 启动线程
t1.start()
t2.start()

# 等待线程结束
t1.join()
t2.join()

print(f"总耗时：{time.time() - start:.1f}秒")

print("\n=== 使用线程池（更简单的写法）===")
start = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(task, "A", 2)
    executor.submit(task, "B", 2)
    executor.submit(task, "C", 1)

print(f"总耗时：{time.time() - start:.1f}秒")

# 4. 多线程 vs 多线程（简单说）
# - 多线程：适合IO密集型任务（网络请求、文件读写、爬虫）
# - 多线程：适合CPU密集型任务（大量计算、图像处理）
# - Python有GIL（全局解释器锁），多线程不能真正并行
# - 想利用多核CPU跑计算，要多进程

import multiprocessing


def cpu_task(n):
    total = 0
    for i in range(n):
        total += i
    return total


print("\n=== 多进程计算（适合CPU密集型）===")
start = time.time()

if __name__ == "__main__":
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(cpu_task, [5000000, 5000000])
        print(f"计算结果：{results}")

    print(f"总耗时：{time.time() - start:.1f}")

print("=" * 30)
print("第20天打卡完成！")
