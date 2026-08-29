# ============ 第四十三天：描述符 + 元类 ============
# 这两个是Python面向对象最深入的内容
# 不要求立刻全懂，先建立概念，后面会越来越清晰

# ============================================================
# 一、描述符 Descriptor
# ============================================================
# 描述符 = 一个类实现了 __get__ / __set__ / __delete__ 中的任一个
# 作用：控制属性的访问、赋值、删除行为

print("=" * 55)
print("  一、描述符 Descriptor")
print("=" * 55)


# --- 先看问题：为什么需要描述符？---

# 需求：Student的score必须0-100，不能乱填
# 笨办法：每个属性都写 if 判断 → 代码重复
# 好办法：用描述符，写一次，到处复用

class ScoreValidator:
    """分数验证描述符：自动检查0-100范围"""

    def __init__(self, min_val=0, max_val=100):
        self.min_val = min_val
        self.max_val = max_val

    # __set_name__: Python 3.6+ 自动调用,直到属性名
    def __set_name__(self, owner, name):
        self.name = name
        self.internal_name = f"_score_{name}"

    # __get__: 读取属性时调用
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.internal_name, None)

    # __set__: 赋值属性时调用
    def __set__(self, obj, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{self.name}必须是数字")
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(
                f"{self.name}必须在{self.min_val}-{self.max_val}之间,"
                f"你传了{value}"
            )
        setattr(obj, self.internal_name, value)


class Student:
    """使用描述符：像普通属性一样用，但自动验证"""

    score = ScoreValidator(0, 100)
    attendance = ScoreValidator(0, 30)  # 出勤天数0-30

    def __init__(self, name, score, attendance):
        self.name = name
        self.score = score  # 赋值时自动触发 __set__ 验证
        self.attendance = attendance

    def __str__(self):
        return f"({self.name}, 分数{self.score}, 出勤={self.attendance}天)"


# 正常使用
s1 = Student("小杰", 92, 28)
print(f"学生：{s1}")
print(f"读取分数：{s1.score}")  # 触发 __get__

# 读取时也走描述符
s2 = Student("李四", 85, 25)
print(f"学生：{s2}")

# 验证：超出范围会报错
try:
    s1.score = 150
except ValueError as e:
    print(f"✗ 验证拦截: {e}")

# 正常修改
s1.score = 88
print(f"修改后分数：{s1}")

# 描述符的本质
print(f"\n描述符原理：")
print(f" s1.score  → 触发 ScoreValidator.__get__(self, s1, Student)")
print(f" s1.score = 88 → 触发 ScoreValidator.__set__(self, s1, 88)")
print(f" 用户感觉不到,但每次访问都走了验证逻辑")


# --- 另一个描述符：自动类型转换 ---

class TypedField:
    """自动类型转换描述符"""

    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self.name}", None)

    def __set__(self, obj, value):
        # 自动转换类型
        try:
            converted = self.expected_type(value)
        except(ValueError, TypeError):
            raise TypeError(f"{self.name}无法转换为{self.expected_type.__name__}")
        setattr(obj, f"_{self.name}", converted)


class Product:
    name = TypedField(str)
    price = TypedField(float)
    quantity = TypedField(int)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} x{self.quantity} =  ¥{self.price * self.quantity:.2f}"


p = Product("Python书", "59.9", "3")  # 传入字符串，自动转类型
print(f"\n产品：{p}")
print(f"  name类型：{type(p.name).__name__}")  # str
print(f"  price类型：{type(p.price).__name__}")  # float
print(f"  quantity类型：{type(p.quantity).__name__}")  # int

# ============================================================
# 二、元类 Metaclass
# ============================================================
# 元类 = 创建类的类
# 普通理解：类是创建对象的模板，元类是创建类的模板

print(f"\n{'=' * 55}")
print("  二、元类 Metaclass")
print("=" * 55)

# --- 先理解：类也是对象 ----
print("\n--- 类也是对象 ---")
print(f"type(42) = {type(42)}")  # <class 'int'>
print(f"type('hi') = {type('hi')}")  # <class 'str'>
print(f"type(Student) = {type(Student)}")  # <class 'type'>
print("→ int/str/Student都是type创建的！type就是元类")

# --- type动态创建类 ---
print("\n--- type动态创建类 ---")


# 普通写法
class Dog:
    def bark(self):
        return "汪汪！"


# type动态创建(等价写法)
Dog2 = type("Dog", (), {"bark": lambda self: "汪汪！"})

d1 = Dog()
d2 = Dog2()
print(f"Dog: {d1.bark()}")
print(f"Dog2: {d2.bark()}")
print("→ 两种写法完全等价，type就是创建类的函数")

# --- 自定义元类 ---
print("\n--- 自定义元类 ---")


class SingletonMeta(type):
    """单例元类：保证一个类只有一个实例"""

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Database(metaclass=SingletonMeta):
    """使用单例元类的数据库类"""

    def __init__(self):
        self.name = "MySQL连接"
        import random
        self.id = random.randint(1000, 9999)

    def __str__(self):
        return f"{self.name}(id={self.id})"


# 创建多个实例, 但都是同一个
db1 = Database()
db2 = Database()
print(f"db1: {db1}")
print(f"db2: {db2}")
print(f"db1 is db2: {db1 is db2}")  # True！同一个实例

# --- 元类实际应用：自动注册 ---
print("\n--- 元类应用：插件自动注册 ---")


class PluginMeta(type):
    """自动注册所有子类的元类"""
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = type.__new__(mcs, name, bases, namespace)
        # 跳过基类， 只注册子类
        if bases:
            PluginMeta.registry[name] = cls
        return cls


class Plugin(metaclass=PluginMeta):
    """插件基类"""

    def run(self):
        raise NotImplementedError


class LogPlugin(Plugin):
    def run(self):
        return "日志插件运行中"


class CachePlugin(Plugin):
    def run(self):
        return "缓存插件运行中"


class AuthPlugin(Plugin):
    def run(self):
        return "认证插件运行中"


print(f"自动注册的插件：{list(PluginMeta.registry.keys())}")
for name, plugin_cls in PluginMeta.registry.items():
    instance = plugin_cls()
    print(f"  {name}: {instance.run()}")


# ===== 总结 =====
print(f"\n{'=' * 55}")
print("  描述符 + 元类 总结")
print("=" * 55)
print("""
描述符：
  - 实现 __get__/__set__ 的类
  - 控制属性的读取/赋值/删除
  - property 就是描述符的语法糖
  - 实战：验证、类型转换、缓存、日志

元类：
  - type 是所有类的元类
  - 自定义元类控制类的创建行为
  - 实战：单例模式、插件注册、ORM框架
  - Django/SQLAlchemy 的核心就是元类
""")

print("第43天打卡完成！Python OOP终极深入！")
