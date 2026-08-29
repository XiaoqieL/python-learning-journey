# ============ 第四十五天：异步爬虫实战 ============
# 对比：同步爬虫 vs 异步爬虫，看速度差距

import time
import asyncio
import aiohttp
import requests
from concurrent.futures import ThreadPoolExecutor

# 测试目标：jsonplaceholder 提供免费API
BASE_URL = "https://jsonplaceholder.typicode.com"
POST_IDS = list(range(1, 11))  # 爬10个帖子


# ============================================================
# 方式1：同步爬虫（传统方式）
# ============================================================
def sync_crawl():
    """同步爬取：一个一个请求"""
    print("=== 同步爬虫(一个一个来) ===")
    results = []
    start = time.time()

    for pid in POST_IDS:
        resp = requests.get(f"{BASE_URL}/posts/{pid}", timeout=10)
        data = resp.json()
        results.append({"id": data["id"], "title": data["title"][:30]})

    elapsed = time.time() - start
    print(f" 爬取{len(results)}条，耗时：{elapsed:.2f}秒")
    for r in results[:3]:
        print(f"    [{r['id']}] {r['title']}...")
    return elapsed


# ============================================================
# 方式2：多线程爬虫（之前学过的方式）
# ============================================================
def thread_crawl():
    """多线程爬取：用线程池"""
    print("=== 多线程爬虫(线程池) ===")

    def fetch(pid):
        resp = requests.get(f"{BASE_URL}/posts/{pid}", timeout=10)
        data = resp.json()
        return {"id": data["id"], "title": data["title"][:30]}

    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch, POST_IDS))

    elapsed = time.time() - start
    print(f"  爬取 {len(results)} 条， 耗时：{elapsed:.2f}秒")
    for r in results[:3]:
        print(f"    [{r['id']}] {r['title']}...")
    return elapsed


# ============================================================
# 方式3：异步爬虫（asyncio + aiohttp）
# ============================================================
async def async_fetch(session, pid):
    """异步获取单个帖子"""
    async with session.get(f"{BASE_URL}/posts/{pid}") as resp:
        data = await resp.json()
        return {"id": data["id"], "title": data["title"][:30]}


async def async_crawl():
    """异步爬取：同时发所有请求"""
    print("\n=== 异步爬虫(asyncio+aiohttp) ===")
    start = time.time()
    results = []

    # 创建aiohttp会话(复用连接，更快)
    async with aiohttp.ClientSession() as session:
        # 同时创建所有协程任务
        tasks = [async_fetch(session, pid) for pid in POST_IDS]
        # gather 同时执行所有任务
        results = await asyncio.gather(*tasks)

    ellipsis = time.time() - start
    print(f"  爬取 {len(results)} 条， 耗时：{ellipsis:.2f}秒")
    for r in results[:3]:
        print(f"     [{r[id]}] {r['title']}...")
    return ellipsis


# ============================================================
# 综合对比
# ============================================================
async def mian():
    print("=" * 55)
    print("  爬虫速度大比拼：同步 vs 多线程 vs 异步")
    print("=" * 55)
    print(f"  目标：爬取 {len(POST_IDS)} 个API接口\n")

    # 1. 同步
    t1 = sync_crawl()

    # 2. 多线程
    t2 = thread_crawl()

    # 3. 异步
    t3 = await async_crawl()

    # 总结
    print(f"\n{'=' * 55}")
    print("  结果对比")
    print("=" * 55)
    print(f"  同步爬虫:   {t1:.2f}秒")
    print(f"  多线程爬虫: {t2:.2f}秒")
    print(f"  异步爬虫:   {t3:.2f}秒")
    print()
    if t1 > 0 and t3 > 0:
        print(f" 异步比同步快：{t1/t3:.1f}倍")
        print(f" 异常比多线程快：{t3/t3:.1f}倍")
    print("=" * 55)

    print("""
      结论：
      - 同步最慢：一个一个请求，时间累加
      - 多线程较快：5个线程并发，但有线程开销
      - 异步最快：单线程内切换，开销极小

      什么时候用异步？
      - 爬虫（大量网络请求）→ aiohttp
      - 接口测试（批量调用API）→ asyncio + aiohttp
      - WebSocket长连接 → websockets库

      什么时候不用异步？
      - CPU密集型计算（用多进程）
      - 简单脚本（同步更直观）
    """)

    print("第45天打卡完成！异步爬虫实战！")


# 运行
if __name__ == "__main__":
    asyncio.run(main())
