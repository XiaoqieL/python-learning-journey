# ============ 第七天：元组tuple + 集合set ============

# --- tuple 元组（不可变，和list像但不能改）---
point = (3, 5)
rgb = (255, 128, 0)
single = (42,)

print(f"坐标：{point}")
print(f"第一个：{point[0]}")
print(f"长度：{len(point)}")
print(f"能否切片：{point[:2]}")

# 尝试修改会报错（了解就行，别执行这行）
# point[0] = 10  # TypeError!

# tuple 和 list 转换
my_list = list(point)
my_list.append(7)
new_tuple = tuple(my_list)
print(f"转换后：{new_tuple}")

print("----")

# --- set 集合（无序，无重复）---
nums = [1, 2, 2, 3, 3, 4]
unique = set(nums)
print(f"去重: {unique}")

s = {5, 1, 3, 7, 1, 5}
print(f"集合: {s}")

#增删
s.add(9)
s.discard(3)
print(f"操作后：{s}")

# 集合运算
a = {1, 2, 3}
b = {3, 4, 5}
print(f"并集：{a | b}")
print(f"交集：{a & b}")
print(f"差集：{a - b}")

print("----")

# --- 小综合：统计一句话每个字出现的次数（dict复习）---
text = "hello world hello python"
words = text.split()
counter = {}
for w in words:
    counter[w] = counter.get(w, 0) + 1
print(f"词频：{counter}")

#7. 第七天打卡
print("=" * 30)
print("第7天打卡完成！")