# ============ 第四十四天：asyncio 协程入门 ============

import asyncio
import time


# ===== 1. 先看：同步代码 =====
# 3个任务，每个1秒，总共3秒

def sync_task(name, seconds):
    print(f"[{name}] 开始")
    time.sleep(seconds)
    print(f"[{name}] 完成")


print("==== 同步执行(一个一个来) ====")
start = time.time()
sync_task("A", 1)
sync_task("B", 1)
sync_task("C", 1)
print(f"总耗时：{time.time() - start:.1f}秒\n")


# ===== 2. 协程：async/await =====
# 3个任务，每个1秒，总共约1秒（并发！）

async def async_task(name, seconds):
    """async函数 = 协程函数"""
    print(f"[{name}] 开始")
    await asyncio.sleep(seconds)  # await = 让出控制权，让其他任务跑
    print(f"[{name}] 完成")


async def mian_async():
    """主协程：同时跑3个任务"""
    start = time.time()
    print("=== 异步执行(并发跑) ====")

    # 方式1：用gather 同时跑多个协程
    await asyncio.gather(
        async_task("A", 1),
        async_task("B", 1),
        async_task("C", 1),
    )

    print(f"总耗时：{time.time() - start:.1f}秒")

# 运行异步程序
asyncio.run(mian_async())

# ===== 3. 核心概念解释 =====
print(f"\n{'=' * 50}")
print("  asyncio 核心概念")
print("=" * 50)
print("""
async def     → 定义一个协程函数（不会立刻执行）
await         → 暂停当前协程，让出CPU给其他协程
asyncio.run() → 启动事件循环，运行协程
asyncio.gather() → 同时跑多个协程，等全部完成

协程 vs 线程：
  - 协程：单线程内切换，开销极小，由代码自己控制切换
  - 线程：操作系统调度，开销大，有GIL限制
  - 适用场景：IO密集型（网络请求、文件读写）

就像餐厅服务员：
  - 同步：等一桌菜做好了再上下一桌 → 慢
  - 异步：点完A桌的菜，去给B桌点单，等菜好了再回来 → 快
""")

# ===== 4. 实战：异步爬取（概念）=====
print("实战场景对比：")
print("  同步爬10个网页：每个1秒，共10秒")
print("  异步爬10个网页：约1秒（同时发请求）")
print("  → 爬虫/接口测试 用 asyncio 速度提升巨大！")

print(f"\n{'=' * 50}")
print("第44天打卡完成！")