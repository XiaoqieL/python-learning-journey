import asyncio
import time


async def fake_fetch(name, delay):
    """模拟网络请求(用sleep代替)"""
    print(f"   [{name}] 请求中...")
    await asyncio.sleep(delay)  # 模拟网络延迟
    print(f" [{name}] 完成！")
    return {"name": name, "data": f"这是{name}的数据"}


async def main():
    print("=== 模拟异步爬虫 ===")

    # 同步方式：2+2+2 = 6秒
    start = time.time()
    r1 = await fake_fetch("A", 2)
    r2 = await fake_fetch("B", 2)
    r3 = await fake_fetch("C", 2)
    print(f"同步耗时：{time.time() - start:.1f}秒\n")

    # 异步方式：max(2,2,2) = 2秒
    start = time.time()
    results = await asyncio.gather(
        fake_fetch("A", 2),
        fake_fetch("B", 2),
        fake_fetch("C", 2),
    )
    print(f"异常耗时：{time.time() - start:.1f}")
    print(f"速度提示3倍！")


asyncio.run(main())
