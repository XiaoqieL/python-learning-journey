# ============ 第四十七天：Python进阶阶段复盘 ============

review = {
    "Day39 魔法方法": [
        "__str__ / __repr__ → print显示",
        "__eq__ / __lt__ → 比较和排序 ",
        "__add__ / __len__ / __getitem__ / __contains__",
    ],
    "Day40 C盘清理工具": [
        "os + pathlib + shutil 实战",
        "dry_run 安全模式设计",
        "PermissionError 跳过无权限文件",
    ],
    "Day41 三大高阶标准库": [
        "collections: Counter / defaultdict / deque / namedtuple",
        "functools: lru_cache / partial / reduce",
        "itertools: chain / permutations / combinations / groupby",
    ],
    "Day42 类型注解+dataclass": [
        "类型注解: str / int / Optional / Union / List / Dict",
        "dataclass 自动生成 __init__/__repr__/__eq__",
        "field(dafault_factory=list) 处理可变默认值",
    ],
    "Day43 描述符+元类": [
        "描述符： __get__/__st__ 控制属性访问",
        "元类：type 创建类,自定义元类控制类创建",
        "实战：单例元类、插件自动注册",
    ],
    "Day44 asyncio协程": [
        "async def / await / asyncio.gather()",
        "协程比线程轻量，单线程切换",
        "适合IO密集型任务",
    ],
    "Day45 异步爬虫实战": [
        "aiohttp 异步爬虫请求",
        "同步 vs 多线程 vs 异步 速度对比",
        "异步比同步快10倍",
    ],
    "Day46 设计模式": [
        "单例模式：全局唯一实例",
        "工厂模式：按类型创建对象",
        "观察者模式：状态变化自动通知",
        "策略模式：随时切换算法",
        "装饰器模式：动态叠加功能",
    ],
}

print("=" * 55)
print("  Python进阶阶段复盘 (Day39-46)")
print("=" * 55)

total = 0
for topic, points in review.items():
    print(f"\n{'-' * 50}")
    print(f" {topic}")
    print(f"{'-' * 50}")
    for p in points:
        print(f"   ✓ {p}")
        total += 1

print(f"\n{'=' * 55}")
print(f"  进阶阶段掌握 {total} 个知识点！")
print(f"{'=' * 55}")

print("""
自我评估（1-5分）：
  1. 魔术方法理解: ___分
  2. 标准库掌握:   ___分
  3. 类型注解:     ___分
  4. 描述符元类:   ___分
  5. 异步编程:     ___分
  6. 设计模式:     ___分

下一步方向：
  - 把不熟悉的点重新看一遍代码
  - 明天开始综合大项目实战
""")

print("第47天打卡完成！")
