# ============ 第四十六天：Python设计模式 ============
# 设计模式 = 前人总结的最佳实践，解决常见问题的模板
# 不需要全背，掌握最常用的5个就够面试和日常用了

from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
import threading

# ============================================================
# 模式1：单例模式（Singleton）
# ============================================================
# 一个类全局只有一个实例
# 场景：数据库连接、配置管理、日志器

print("=" * 55)
print("  模式1：单例模式")
print("=" * 55)


# 方式A：用装饰器实现单例
def singleton(cls):
    """单例装饰器"""
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Config:
    def __init__(self):
        self.settings = {"env": "test", "debug": True}

    def get(self, key):
        return self.settings.get(key)


c1 = Config()
c2 = Config()
print(f"c1 is c2: {c1 is c2}")  # True, 同一个实例


# 方式B：用__new__实现单例
class Logger:
    _instance = None
    _lock = threading.Lock()  # 线程安全

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'logs'):
            self.logs = []

    def log(self, msg):
        self.logs.append(msg)


log1 = Logger()
log2 = Logger()
log1.log("测试1")
log2.log("测试2")
print(f"Logger同一个实例：{log1 is log2}")
print(f"日志：{log1.logs}")

# ============================================================
# 模式2：工厂模式（Factory）
# ============================================================
# 用一个工厂函数/类来创建对象，不直接new
# 场景：根据不同类型创建不同对象

print(f"\n{'=' * 55}")
print("  模式2：工厂模式")
print("=" * 55)


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "汪汪汪!"


class Cat(Animal):
    def speak(self):
        return "喵喵喵!"


class Duck(Animal):
    def speak(self):
        return "嘎嘎嘎!"


class AnimalFactory:
    """动物工厂：根据类型创建对应的动物"""
    _registry = {"dog": Dog, "cat": Cat, "duck": Duck}

    @classmethod
    def create(cls, animal_type: str) -> Animal:
        animal_class = cls._registry.get(animal_type)
        if not animal_class:
            raise ValueError(f"不支持的动物类型：{animal_type}")
        return animal_class()


# 使用：不需要知道具体类名，传类型字符串就行
for t in ["dog", "cat", "duck"]:
    animal = AnimalFactory.create(t)
    print(f"{t}：{animal.speak()}")

# ============================================================
# 模式3：观察者模式（Observer）
# ============================================================
# 一个对象变化时，自动通知所有观察者
# 场景：事件系统、消息推送、状态监控

print(f"\n{'=' * 55}")
print("  模式3：观察者模式")
print("=" * 55)


class Subject:
    """被观察的主题"""

    def __init__(self):
        self._observers = []
        self.state = None

    def attach(self, observer):
        """注册观察者"""
        self._observers.append(observer)

    def detach(self, observer):
        """移除观察者"""
        self._observers.remove(observer)

    def notify(self):
        """通知所有观察者"""
        for observer in self._observers:
            observer.update(self.state)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()  # 状态变化时自动通知


class Observer:
    """观察者基类"""

    def __init__(self, name):
        self.name = name

    def update(self, state):
        print(f" [{self.name}] 收到通知：{state}")


# 实战：订单状态变化通知
class OrderStatus(Subject):
    """订单状态(被观察者)"""

    def __init__(self, order_id):
        super().__init__()
        self.order_id = order_id

    def change_status(self, new_status):
        print(f"\n订单{self.order_id} 状态变为：{new_status}")
        self.state = new_status  # 触发notify


# 创建订单和观察者
order = OrderStatus("ORD-001")
sms_notifier = Observer("短信通知")
email_notifier = Observer("邮件通知")
log_notifier = Observer("日志记录")

# 注册观察者
order.attach(sms_notifier)
order.attach(email_notifier)
order.attach(log_notifier)

# 状态变化 → 自动通知所有人
order.change_status("已付款")
order.change_status("已发货")
order.change_status("已签收")

# ============================================================
# 模式4：策略模式（Strategy）
# ============================================================
# 把不同算法封装成独立类，可以随时切换
# 场景：支付方式选择、排序算法切换、折扣计算

print(f"\n{'=' * 55}")
print("  模式4：策略模式")
print("=" * 55)


class DiscountStrategy(ABC):
    """折扣策略基类"""

    @abstractmethod
    def calculate(self, price: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def calculate(self, price):
        return price


class TenPercentOff(DiscountStrategy):
    def calculate(self, price):
        return price * 0.9


class FullReduction(DiscountStrategy):
    """满200减30"""

    def calculate(self, price):
        return price - 30 if price >= 200 else price


class VIPDiscount(DiscountStrategy):
    """VIP打7折"""

    def calculate(self, price):
        return price * 0.7


class ShoppingCart:
    """购物车：使用不同的折扣策略"""

    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy
        self._items: List[Dict] = []

    def set_strategy(self, strategy: DiscountStrategy):
        """随时切换策略"""
        self.strategy = strategy

    def add_item(self, name, price):
        self._items.append({"name": name, "price": price})

    def checkout(self):
        total = sum(item["price"] for item in self._items)
        discounted = self.strategy.calculate(total)
        return {"original": total, "discounted": discounted}


cart = ShoppingCart(NoDiscount())
cart.add_item("Python书", 59)
cart.add_item("键盘", 199)
result = cart.checkout()
print(f"无折扣：原价{result['original']} → 实付{result['discounted']}")

cart.set_strategy(TenPercentOff())
result = cart.checkout()
print(f"9折：   原价{result['original']} → 实付{result['discounted']}")

cart.set_strategy(FullReduction())
result = cart.checkout()
print(f"满减：  原价{result['original']} → 实付{result['discounted']}")

cart.set_strategy(VIPDiscount())
result = cart.checkout()
print(f"会员7折：   原价{result['original']} → 实付{result['discounted']}")

# ============================================================
# 模式5：装饰器模式（Decorator）
# ============================================================
# 动态给对象添加新功能，不修改原代码
# 场景：给函数加日志、缓存、权限检查

print(f"\n{'=' * 55}")
print("  模式5：装饰器模式（类版）")
print("=" * 55)


class Coffee:
    """基础咖啡"""

    def cost(self):
        return 15

    def description(self):
        return "基础咖啡"


class CoffeeDecorator:
    """咖啡装饰器基类"""

    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


class MilkDecorator(CoffeeDecorator):
    """加牛奶"""

    def cost(self):
        return self._coffee.cost() + 5

    def description(self):
        return self._coffee.description() + "加牛奶"


class SugarDecorator(CoffeeDecorator):
    """加糖"""

    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + "加糖"


class CreamDecorator(CoffeeDecorator):
    """加奶油"""

    def cost(self):
        return self._coffee.cost() + 8

    def description(self):
        return self._coffee.description() + "加奶油"


# 组合技使用：想要什么就包什么
coffee = Coffee()
print(f"  {coffee.description()}: ¥{coffee.cost()}")

coffee = MilkDecorator(coffee)  # 加牛奶
print(f"  {coffee.description()}:  ¥{coffee.cost()}")

coffee = SugarDecorator(coffee)  # 加糖
print(f"  {coffee.description()}:  ¥{coffee.cost()}")

coffee = CreamDecorator(coffee)  # 加奶油
print(f"  {coffee.description()}:  ¥{coffee.cost()}")

# ===== 总结 =====
print(f"\n{'=' * 55}")
print("  5大设计模式总结")
print("=" * 55)
print("""
模式       一句话            常见场景
─────────────────────────────────────
单例模式    全局只有一个实例   数据库连接、配置
工厂模式    根据类型创建对象    支付方式、动物创建
观察者模式  状态变化自动通知    事件系统、消息推送
策略模式    随时切换算法        折扣计算、排序
装饰器模式  动态添加功能        日志、缓存、权限

面试技巧：
- 被问"你用过什么设计模式？"
- 答："我用过单例模式做配置管理，工厂模式做对象创建，
       策略模式做折扣计算，装饰器模式做日志和缓存"
""")

print("第46天打卡完成！设计模式入门！")
