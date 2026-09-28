import json, os


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

    def save(self):
        # 把 self.records 保存到 json 文件中
        json.dump(self.records, open(self.file, mode="w", encoding="utf-8"), ensure_ascii=False)
        pass

    def add(self, name, amount):
        # 记一笔：self.records[name] = 已有 + amount(用get)
        self.records[name] = self.records.get(name, 0) + amount

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


if __name__ == "__main__":
    acc = Account()  # 创建即自动读入上次数据
    while True:
        print("\n1.记一笔  2.查看  3.总支出  4.删除  0.退出")
        choice = input("请选择: ").strip()

        if choice == "1":
            name = input("项目: ").strip()
            try:
                amount = float(input("金额: "))
            except ValueError:
                print("金额必须是数字")
                continue
            acc.add(name, amount)  # ← 调用类的方法

        elif choice == "2":
            acc.show()  # ← 调用类的方法

        elif choice == "3":
            print(f"总支出: ¥{acc.total():.2f}")  # ← 调用类的方法

        elif choice == "4":
            name = input("要删除的项目: ").strip()
            acc.delete(name)  # ← 调用类的方法

        elif choice == "0":
            acc.save()  # ← 退出前保存
            print("已保存，再见")
            break

        else:
            print("无效选项，请重选")
