# ============ 第四十一天：三大高阶标准库 ============

# ============================================================
# 一、collections：高级容器，比 list/dict 更强大
# ============================================================

from collections import Counter, defaultdict, OrderedDict, deque, namedtuple

print("=" * 50)
print("  一、collections 模块")
print("=" * 50)

# 1. Counter: 自动计数器(统计频率神器)
print("\n--- Counter 统计频率 ---")
text = "the quick brown fox jumps over the lazy dog the end"
words = text.split()
counter = Counter(words)
print(f"词频统计：{counter}")
print(f"'the'出现次数：{counter['the']}")
print(f"最多的3个词：{counter.most_common(3)}")

# 字符频率
letters = Counter("abracadabra")
print(f"字母频率：{letters.most_common(3)}")

# 2. defaultdict: 带默认值的字典(告别 KeyError)
print("\n--- defaultdict ---")
# 普通字典取不存在的key会报错, defaultdict不会
scores = defaultdict(list)  # 默认值是空列表
students_data = [
    ("张三", 85), ("李四", 90), ("张三", 78), ("王五", 92), ("李四", 88)
]
for name, score in students_data:
    scores[name].append(score)  # 不同判断key存不存在 ！

print(f"张三成绩：{scores['张三']}")
print(f"李四成绩：{scores['李四']}")
print(f"不存在的人：{scores['赵六']}")  # 返回[]不报错

# 3. OrderedDict: 有序字典(Python3.7+ dict已经有序，但OrderedDict有额外功能)
print("\n--- OrderedDict ---")
od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3
print(f"有序字典：{list(od.keys())}")
od.move_to_end("first")  # 把first移到末尾
print(f"移动后：{list(od.keys())}")

# 4. deque：双端队列(头尾都能快速增删,list只能尾增)
print("\n--- deque 双端队列 ---")
dq = deque([1, 2, 3])
dq.appendleft(0)  # 头部插入 O(1)，list的insert(0)是O(n)
dq.append(4)  # 尾部插入 O(1)
print(f"deque：{dq}")
print(f"pop左：{dq.popleft()}")
print(f"pop右：{dq.pop()}")
print(f"剩余：{dq}")

# deque做队列(先进先出)
queue = deque(["任务1", "任务2", "任务3"])
print(f" 处理：{queue.popleft()}")  # 取出第一个
print(f"剩余队列：{list(queue)}")

# 5. namedtuple: 具名元组(比class轻量, 比tuple可读)
print("\n--- namedtuple ---")
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"点：{p}")
print(f"x = {p.x}, y = {p.y}")  # 用名字访问，不用 p[0]
print(f"元组方式：x={p[0]}, y={p[1]}")  # 也支持索引

# ============================================================
# 二、functools：函数工具箱
# ============================================================


from functools import lru_cache, partial, reduce, wraps

print(f"\n{'=' * 50}")
print("  二、functools 模块")
print("=" * 50)

# 1. lru_cache：自动缓存函数结果（递归/重复计算神器）
print("\n --- lru_cache 缓存 ---")


@lru_cache(maxsize=128)
def fib(n):
    """斐波那契数列 - 加了缓存后速度飞快"""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(f" fib(50) = {fib(50)}")  # 没缓存会算很久，有缓存秒出
print(f"缓存信息：{fib.cache_info()}")

# 2. partial：偏函数, 固定部分参数
print("\n --- partial 偏函数 ---")


def power(base, exp):
    return base ** exp


# 创建一个固定exp的"新函数"
square = partial(power, exp=2)
cube = partial(power, exp=3)
print(f"square(5) = {square(5)}")  # 25
print(f"cube(3) = {cube(3)}")  # 27

# 3. reduce: 累计运算
print("\n --- reduce 累计运算 ---")
from operator import add

nums = [1, 2, 3, 4, 5]
# reduce: ((1+2)+3)+4)+5
total = reduce(add, nums)
print(f"reduce求和：{total}")
# 等价于 sum(nums), 但reduce可以做更复杂的累积

# reduce实现阶乘
product = reduce(lambda x, y: x * y, range(1, 6))
print(f"5的阶乘：{product}")

# ============================================================
# 三、itertools：迭代器工具箱
# ============================================================

from itertools import chain, cycle, repeat, product as iproduct, permutations, combinations, groupby, islice

print(f"\n{'=' * 50}")
print("  三、itertools 模块")
print("=" * 50)

# 1. chain: 连接多个迭代器
print("\n --- chain 拼接 ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
chained = list(chain(list1, list2, list3))
print(f"拼接：{chained}")  # [1,2,3,4,5,6,7,8,9]

# 2. cycle: 无限循环
print("\n--- cycle 无限循环 ----")
colors = cycle(["红", "绿", "蓝"])
for i in range(7):
    print(f"  {next(colors)}", end=" ")
print(f"无限循环取前7个")

# 3. permutations: 全排列
print("\n--- permutations 全排列 ---")
perms = list(permutations("ABC", 2))  # 从ABC取2个排列
print(f"AB取2排列：{perms}")  # 6种

# 4. combinations: 组合
print("\n--- combinations 组合 ---")
combs = list(combinations("ABC", 2))
print(f"AB取2组合：{combs}")  # 3种（不讲究顺序）

# 5. product: 笛卡尔积
print("\n--- product 笛卡尔积 ---")
sizes = ["S", "M", "L"]
colors_list = ["红", "蓝"]
combos = list(iproduct(sizes, colors_list))
print(f"尺码×颜色：{combos}")  # 6种组合

# 6. groupby: 分组
print("\n--- groupby 分组 ---")
students = [
    ("一班", "张三"), ("二班", "李四"), ("一班", "王五"),
    ("二班", "赵六"), ("三班", "钱七"), ("一班", "孙八")
]
students.sort(key=lambda x: x[0])  # 先按班级排序
for class_name, group in groupby(students, key=lambda x: x[0]):
    names = [g[1] for g in group]
    print(f" {class_name}: {names}")

# 7. islice: 切片迭代器（对生成器切片）
print("\n--- islice 切片迭代器 ---")


def naturals():
    n = 1
    while True:
        yield n
        n += 1


# 取到5到8个自然数
sliced = list(islice(naturals(), 4, 8))
print(f"自然数5-8：{sliced}")

# ===== 综合实战 =====
print(f"\n{'=' * 50}")
print("  综合实战：统计文章词频 + 排序")
print("=" * 50)

article = """
Python is great Python is powerful
Python can do web development
Python can do data science
Python can do automation
Python is everywhere
"""

# 一行代码搞定词频统计
word_count = Counter(article.lower().split())
print(f"\n词频TOP5:")
for word, count in word_count.most_common(5):
    bar = "█" * count
    print(f"   {word:<15} {bar} {count}次")

print(f"\n第41天打卡完成！")