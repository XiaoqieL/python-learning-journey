# 学生数据模型

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "优秀"
        elif self.score >= 80:
            return "良好"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "score": self.score,
            "grade": self.get_grade()
        }

    def __str__(self):
        return f"Student({self.name}, {self.age}岁, {self.score}分, {self.get_grade()})"
