# ============ 第三十九天：Python魔术方法 ============
# 魔术方法 = 以双下划线开头和结尾的方法，如 __init__、__str__
# 它们让自定义类支持 Python 内置操作（print、len、+、比较等）

class Student:
    """一个完整的示例：用魔术方法让类更好用"""

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    # __str__: print(对象)时显示什么
    def __str__(self):
        return f"Student({self.name}, {self.age}岁, {self.score}分)"

    # __repr__: 在列表/交互式环境中显示什么
    def __repr__(self):
        return f"Student('{self.name}', {self.age}, {self.score})"

    # __eq__: 支持 == 比较
    def __eq__(self, other):
        return self.score == other.score

    # __lt__: 支持 < 比较（排序就靠它）
    def __lt__(self, other):
        return self.score < other.score

    # __len__: 支持 len(对象)
    def __len__(self):
        return len(self.name)

    # __add__: 支持 对象+对象
    def __add__(self, other):
        return self.score + other.score

    # __getitem__: 支持 对象[索引]取值
    def __getitem__(self, key):
        data = {"name": self.name, "age": self.age, "score": self.score}
        return data.get(key, f"无此字段：{key}")

    # __contains__: 支持 in 关键字
    def __contains__(self, keyword):
        return keyword in self.name


# ===== 测试所有魔术方法 =====

s1 = Student("小杰", 28, 92)
s2 = Student("李四", 25, 78)
s3 = Student("王五", 27, 92)

# __str__: print 能直接打印对象
print(f"print(s1):{s1}")  # Student(小杰, 28岁, 92分)

# __repr__: 放在列表里显示
print(f"列表显示：{[s1, s2, s3]}")

# __eq__: 支持 == 比较
print(f"s1 == s3(同分)：{s1 == s3}")
print(f"s1 == s2: {s1 == s2}")

# __lt__: 支持 < 比较 → 排序
students = [s1, s2, s3]
students.sort()
print(f"排序后：{[s.name for s in students]}")

# __len__: 支持 len()
print(f"len(s1): {len(s1)}")

# __add__: 支持 + 运算
print(f"s1 + s2 + s3 = {s1 + s2 + s3}")

# __getitem__: 支持 [] 取值
print(f"s1['name']: {s1['name']}")
print(f"s1['age']: {s1['age']}")
print(f"s1['xxx']: {s1['xxx']}")

# __contains__: 支持 in 关键字
print(f"'小' in s1: {'小' in s1}")
print(f"'大' in s1: {'大' in s1}")

# ===== 总结：魔术方法的威力 =====
print(f"\n{'=' * 50}")
print("魔术方法让你的类像内置类型一样好用：")
print("  __str__    → print(对象) 友好显示")
print("  __repr__   → 调试/列表显示")
print("  __eq__     → 支持 == 比较")
print("  __lt__     → 支持 < 比较和排序")
print("  __len__    → 支持 len()")
print("  __add__    → 支持 + 运算")
print("  __getitem__ → 支持 [] 索引")
print("  __contains__ → 支持 in 关键字")
print(f"{'=' * 50}")

print("\n第39天打卡完成！")
