# ============ 第四十二天：类型注解 + dataclass ============

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Union, Callable, Any, Tuple
from datetime import datetime

# ============================================================
# 一、类型注解：给Python加类型提示（不强制，但IDE会检查）
# ============================================================

print("=" * 50)
print("  一、类型注解 Type Hints")
print("=" * 50)

# 1. 基本类型注释
name: str = "小杰"
age: int = 28
score: float = 92.5
is_pass: bool = True


# Python 不强制检查类型， 但IDE（如PyCharm）会提示
# name = 123  # IDE会标黄警告！

# 2. 函数类型注解
def greet(name: str, times: int = 1) -> str:
    """参数：str和int, 返回值：str"""
    return f"Hello {name}!" * times


result: str = greet("Python", 2)
print(f"greet: {result}")


# 3. 复杂类型注解
def process_scores(scores: List[int]) -> Dict[str, float]:
    """接受int列表, 返回str->float的字典"""
    return {
        "avg": sum(scores) / len(scores),
        "max": float(max(scores)),
        "min": float(min(scores))
    }


stats: Dict[str, float] = process_scores([85, 92, 78, 95, 60])
print(f"统计：{stats}")


# 4. Optional: 可能为None
def find_user(user_id: int) -> Optional[str]:
    """返回str或None"""
    users = {1: "张三", 2: "李四"}
    return users.get(user_id)  # 找不到返回NOne


user: Optional[str] = find_user(3)
print(f"查找用户：{user}")  # None


# 5. Union: 可能是多个类型之一
def parse_value(val: Union[int, str]) -> int:
    """参数可以是int或str"""
    if isinstance(val, str):
        return int(val)
    return val


print(f"parse('42'): {parse_value('42')}")
print(f"parse(42): {parse_value(42)}")


# 6. Tuple: 固定长度元组类型
def get_point() -> Tuple[float, float, float]:
    return (10.5, 20.3, 30.0)


x, y, z = get_point()
print(f"点坐标：x=({x}, y={y}, z={z})")


# 7. Callable: 函数类型
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    """接受一个(int, int)->int的函数"""
    return func(a, b)


print(f"apply(add, 3, 5): {apply(lambda x, y: x + y, 3, 5)}")


# 8.Any: 任意类型(尽量少用，等于不注释)
def mystery(data: Any) -> Any:
    return data


# ============================================================
# 二、dataclass：用装饰器自动生成类代码
# ============================================================

print(f"\n{'=' * 50}")
print("  二、dataclass 数据类")
print("=" * 50)


# 普通写法(Day11学过的)
class OldStudent:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"({self.name}, {self.age}, {self.score})"


# dataclass写法：自动生成 __init__、__repr__、__eq__
@dataclass
class Student:
    name: str
    age: int
    score: float = 0.0  # 默认值
    tags: List[str] = field(default_factory=list)  # 可变默认值必须用field


# 使用(和普通类一样)
s1 = Student("小杰", 28, 92.5)
s2 = Student("李四", 25, 85.0)
s3 = Student("小杰", 27, 78.0)

print(f"s1:{s1}")
print(f"s1 == s3: {s1 == s3}")
print(f"s1 != s2: {s1 != s2}")


# field的高级用法
@dataclass
class Course:
    title: str
    price: float
    students: List[str] = field(default_factory=list)  # 默认空列表
    metadata: Dict[str, Any] = field(default_factory=dict)  # 默认空字典
    _id: int = field(default=0, repr=False, compare=False)  # 不显示不比较


c1 = Course("Python进阶", 299.9)
c1.students.extend(["张三", "李四"])
print(f"\n课程：{c1}")
print(f"学生：{c1.students}")


# frozen dateclass: 不可变(像tuple一样)
@dataclass(frozen=True)
class Point:
    x: float
    y: float


p1 = Point(1.0, 2.0)
print(f"\n点：{p1}")
# p1.x = 10 # 报错！frozen不可修改
print("frozen的dataclass不可修改")

# ===== 对比总结 =====
print(f"\n{'=' * 50}")
print("  类型注解 + dataclass 的好处")
print("=" * 50)
print("""
1. IDE自动补全和类型检查 → 减少bug
2. 代码可读性更强 → 一眼看出参数类型
3. dataclass自动生成 __init__/__repr__/__eq__
4. 大厂项目标配（FastAPI/Pydantic都依赖类型注解）
5. 静态检查工具mypy可以在运行前发现类型错误
""")

# __future__注解（Python 3.10+的写法更简洁）
# from __future__ import annotations
# 这样 List[int] 可以直接写 list[int]，Dict[str, int] 写 dict[str, int]

print("第42天打卡完成！")
