第41天：三大高阶标准库 速查表
配套文件：day41_adv_stdlib.py

一、collections — 高级容器

Python

1
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict
类	导入方式	常用方法 / 属性	示例
Counter 计数器	Counter(可迭代对象)	.most_common(n) 前n名
.get(key, 0) 取次数	Counter("abracadabra").most_common(3)
defaultdict 默认字典	defaultdict(类型) 如 list/int/set	和普通 dict 一样用，取不存在的 key 返回默认值	d = defaultdict(list)
d["a"].append(1) 不用判断 key
deque 双端队列	deque(列表)	.append(x) 尾部加
.appendleft(x) 头部加
.pop() 尾部删
.popleft() 头部删	dq = deque([1,2,3])
dq.appendleft(0) → [0,1,2,3]
namedtuple 具名元组	namedtuple("类名", ["字段1","字段2"])	用 .字段名 访问，也支持下标	Point = namedtuple("Point",["x","y"])
p = Point(10,20) → p.x = 10
OrderedDict 有序字典	OrderedDict()	.move_to_end(key) 移到末尾
.popitem(last=True) 删最后一个	od.move_to_end("first")
二、functools — 函数工具

Python

1
from functools import lru_cache, partial, reduce, wraps
工具	用法	作用	示例
@lru_cache	装饰器，加在函数上	缓存函数结果，相同参数直接返回	@lru_cache(maxsize=128)
def fib(n): ...
fib(50) 秒出
partial	partial(函数, 参数=固定值)	固定部分参数，造一个新函数	square = partial(pow, exp=2)
square(5) → 25
reduce	reduce(函数, 列表)	累计运算（两两合并成一个）	reduce(lambda x,y: x*y, range(1,6)) → 120（阶乘）
wraps	装饰器内部用	保留原函数的名字和文档	写装饰器时用
三、itertools — 迭代器工具

Python

1
from itertools import chain, cycle, permutations, combinations, product, groupby, islice, repeat
工具	用法	作用	示例
chain	chain(列表1, 列表2, ...)	拼接多个迭代器	chain([1,2],[3,4]) → [1,2,3,4]
cycle	cycle(列表)	无限循环迭代	cycle(["红","绿","蓝"]) 轮流取
permutations	permutations(元素, 取几个)	全排列（讲究顺序）	permutations("ABC",2) → 6种
combinations	combinations(元素, 取几个)	组合（不讲究顺序）	combinations("ABC",2) → 3种
product	product(列表1, 列表2)	笛卡尔积（所有组合）	product(["S","M"],["红","蓝"]) → 6种
groupby	groupby(列表, key=函数)	按 key 分组（必须先排序）	groupby(students, key=lambda x: x[0])
islice	islice(迭代器, start, end)	对生成器切片	islice(gen, 4, 8) 取第5到第8个
repeat	repeat(x, 次数)	重复生成同一个值	repeat(10, 3) → [10,10,10]
四、快速选型表
不知道用哪个工具时，查表：

我想做什么	用什么
统计词频 / 次数排行	Counter + .most_common()
按类别分组（不用判断key存不存在）	defaultdict(list)
列表头部频繁插入删除	deque
轻量数据结构，不想写 class	namedtuple
递归太慢，想加速	@lru_cache
函数参数太多，想固定几个	partial
阶乘 / 累乘 / 累积运算	reduce
多个列表拼在一起遍历	chain
排列组合问题	permutations / combinations
尺码×颜色 所有组合	product
按班级/类别分组	groupby（先排序！）
无限生成器取前几个	islice
五、记忆口诀
Counter = 统计神器，most_common 一把梭
defaultdict = 分组神器，告别 KeyError
lru_cache = 加速神器，递归必备
permutations = 排列（顺序有关）
combinations = 组合（顺序无关）
groupby = 分组神器，但记得先排序
六、掌握程度建议
优先级	工具	掌握程度
🌟🌟🌟 必须会	Counter、defaultdict	能自己写出来
🌟🌟 熟悉	lru_cache、partial、permutations、combinations	知道有这东西，用时能查
🌟 了解	deque、namedtuple、reduce、chain、groupby、islice、cycle、product	有印象，知道能解决什么问题