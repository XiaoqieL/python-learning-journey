# ============ 第十一天：面向对象基础 ============

# 1. 什么是类和对象？
# 类 = 模板（比如"学生"这个概念）
# 对象 = 具体的人（比如"小杰"、"李四"）

# 2. 定义第一个类
class Student:
    # __init__() 方法是类的构造方法，在创建对象时自动调用
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # 方法(函数写在类里就叫方法)
    def introduce(self):
        print(f"我叫{self.name}, {self.age}岁, 考了{self.score}分")

    def is_pass(self):
        return self.score >= 60


# 3. 创建对象
s1 = Student("小杰", 28, 90)
s2 = Student("李四", 25, 55)
s3 = Student("王五", 27, 78)

# 4. 使用对象
s1.introduce()
s2.introduce()
s3.introduce()

# 5. 调用方法判断
for s in [s1, s2, s3]:
    status = "通过" if s.is_pass() else "挂科"
    print(f"{s.name}: {status}")

print("-----")


# 6. 继承 -- 父类
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name}: {self.sound}")


# 7. 继承 -- 子类（括号里写父类）
class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

    def fetch(self):
        print(f"{self.name}去捡球了！")


class Cat(Animal):
    def climb(self):
        print(f"{self.name}爬到了柜子上!")


# 8. 使用继承
dog = Dog("旺财", "汪汪", "金毛")
cat = Cat("咪咪", "喵喵")

dog.speak()  # 继承来的方法
dog.fetch()  # 自己的方法
cat.speak()
cat.climb()

print("------")


# 9. 实战: 成绩管理系统(结合OOP + 列表 + 字典 + 文件)
class ScoreManager:
    def __init__(self):
        self.students = []

    def add(self, name, score):
        self.students.append({"name": name, "score": score})

    def remove(self, name):
        self.students.remove({"name": name})

    def search(self, name):
        for s in self.students:
            if s['name'] == name:
                return s


    def show_all(self):
        for s in self.students:
            grade = self._get_grade(s["score"])
            print(f"{s['name']}: {s['score']}分 ({grade})")

    def get_average(self):
        if not self.students:
            return 0
        total = sum(s["score"] for s in self.students)
        return total / len(self.students)

    def get_top(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s["score"])

    def _get_grade(self, score):
        if score >= 90:
            return "优秀"
        elif score >= 80:
            return "良好"
        elif score >= 60:
            return "及格"
        else:
            return "不及格"

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for s in self.students:
                f.write(f"{s['name']}, {s['score']}\n")
        print(f"已保存到{filename}")


# 使用成绩管理系统
mgr = ScoreManager()
mgr.add("小杰", 92)
mgr.add("李四", 55)
mgr.add("王五", 78)
mgr.add("赵六", 88)
mgr.add("钱七", 63)

print("==== 删除 =====")
mgr.remove("钱七")

print("===== 搜索 =====")
mgr.search("小杰")

print("==== 全部成绩 =====")
mgr.show_all()

print(f"\n平均分：{mgr.get_average():.1f}")

top = mgr.get_top()
print(f"最高分: {top['name']} - {top['score']}分")

mgr.save_to_file("day11_scores.txt")

# ---- 举一反三练习区 ----
# 试试自己改：
# 1. 给 ScoreManager 加一个 remove(name) 方法删除学生
# 2. 加一个 search(name) 方法按姓名查找
