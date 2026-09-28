class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show(self):
        print(f"姓名: {self.name}, 分数: {self.score}")

    def is_pass(self):
        return self.score >= 60


# ----数据----
student_data = [('张三', 90), ('李四', 80), ('王五', 50)]

# ---- 批量创建----
students = []
for name, score in student_data:
    students.append(Student(name, score))

# -----批量展示----
for stu in students:
    stu.show()
    print(f"及格: {stu.is_pass()}")
