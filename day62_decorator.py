import time
import json, os


def say_hello():
    print("你好")


def call_twice(func):  # 函数作为参数
    func()
    func()


call_twice(say_hello)  # 会打印两次"你好"


def timing(func):
    """装饰器:给函数加耗时统计"""

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # 调用原函数
        cost = time.time() - start
        print(f"耗时:{cost:.4f} 秒")
        return result

    return wrapper


class Account:
    def __init__(self, file="account.json"):
        self.file = file  # 数据文件名
        self.records = {}  # 记账字典{项目:金额}
        self.load()  # 启动时自动读文件

    def load(self):
        if os.path.exists(self.file):
            try:
                self.records = json.load(open(self.file, encoding="utf-8"))
            except json.JSONDecodeError:
                print("警告: 数据文件损坏或为空，已重新开始")
                self.records = {}
        pass

    @timing
    def save(self):
        # 把 self.records 保存到 json 文件中
        json.dump(self.records, open(self.file, mode="w", encoding="utf-8"), ensure_ascii=False)
        pass

    @timing
    def add(self, name, amount):
        # 记一笔：self.records[name] = 已有 + amount(用get)
        self.records[name] = self.records.get(name, 0) + amount

    @timing
    def delete(self, name):
        # 删除一条(pop, 不存在就提示)
        if name in self.records:
            self.records.pop(name)
        else:
            print(f"{name}不存在")
        pass

    def total(self):
        # 返回总金额 sum(self.records.values())
        return sum(self.records.values())

    def show(self):
        # 打印所有记录
        for k, v in self.records.items():
            print(f"{k} ¥{v:.2f}")


@timing
def slow_job():
    time.sleep(1)


slow_job()

if __name__ == "__main__":
    slow_job()  # 输出耗时
    acc = Account()
    acc.add("购物", 100)
    acc.add("购物", 10)
    acc.save()
    print(f"总支出: ¥{acc.total():.2f}")
