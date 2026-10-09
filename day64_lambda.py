def add(x, y):
    return x + y


# 同样的功能，lambda 写法
add2 = lambda x, y: x + y

print(add(3, 5))  # 8
print(add2(3, 5))  # 8

# 学生数据:(姓名,分数)的列表
students = [("张三", 80), ("李四", 95), ("王五", 50)]

# 按分数排序(从小到大):key 告诉 sorted "拿每项的那个字段来比"
by_score = sorted(students, key=lambda item: item[1])
print(by_score)

# 倒序
by_score_desc = sorted(students, key=lambda item: item[1], reverse=True)
print(by_score_desc)

# 分数最高之人
top = max(students, key=lambda item: item[1])
print(top)
