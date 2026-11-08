from functools import reduce

students = [("张三", 85), ("李四", 55), ("王五", 92), ("赵六", 70), ("钱七", 45)]

passed = list(filter(lambda x: x[1] >= 60, students))
bonus = list(map(lambda x: (x[0], x[1] + 5), passed))
total = reduce(lambda a, b: a + b[1], bonus, 0)

print(passed)
print(bonus)
print(total)
