class Student:
    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def show(self):
        print(f"姓名: {self.name}, 分数: {self.score}")

    def is_pass(self):
        return self.score >= 60

    def __str__(self):
        return f"学生{self.name}，分数:({self.score})"


class TopStudent(Student):
    def __init__(self, name, score, level):
        super().__init__(name, score, level)

    def award(self):
        return f"{self.name} 获得{self.level}奖学金"


stu1 = Student("张三", 90, "一等")
top = TopStudent("王五", 80, "二等")
print(top.award())
print(top)
print(top.is_pass())

print(stu1)
