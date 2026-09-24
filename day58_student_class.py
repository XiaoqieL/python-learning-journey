class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show(self):
        print(f"姓名: {self.name}, 分数: {self.score}")

    def is_pass(self):
        return self.score >= 60


stu1 = Student('张三', 90)
stu2 = Student('李四', 80)
stu3 = Student('王五', 50)
stu1.show()
stu2.show()
stu3.show()
print(stu1.is_pass())
print(stu2.is_pass())
print(stu3.is_pass())
