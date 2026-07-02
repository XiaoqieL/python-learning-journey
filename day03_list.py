# ============ 第三天：列表 list 全套操作 ============

#1. 创建列表
nums = [10, 20, 30, 40, 50]
names = ["张三", "李四", "王五"]
empty = []
print(nums)
print(names)

# 2. 增---添加元素
nums.append(60)
nums.insert(0, 5)
print(f"添加后：{nums}")

nums2 = [70, 80]
nums.extend(nums2)
print(f"合并后：{nums}")

#3. 删--删除元素
nums.remove(60)
print(f"remove后：{nums}")

popped = nums.pop()
print(f"pop弹出的：{popped}, 剩余：{nums}")

del nums[0]
print(f"del后：{nums}")

#4. 改--修改元素
names[0] = "赵六"
print(f"修改后：{names}")


#5. 查--访问和查询
print(f"第一个：{nums[0]}")
print(f"最后一个：{nums[-1]}")
print(f"长度：{len(nums)}")
print(f"30在不在：{30 in nums}")
print(f"100在不在：{100 in nums}")
print(f"20的位置：{nums.index(20)}")

#6. 排序
scores = [85, 92, 78, 95, 60, 88]
scores.sort()
print(f"升序：{scores}")
scores.sort(reverse=True)
print(f"降序：{scores}")


#7. 切片
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"前三个：{a[0:3]}")
print(f"后三个：{a[-3:]}")
print(f"中间3个：{a[3:6]}")
print(f"每隔一个：{a[::2]}")

#8. 循环 + 列表实战：1到100累加（复习循环）
total = 0
for i in range(1, 101):
    total += i
print(f"1到100的和：{total}")

#9. 列表推导式
squares = [i ** 2 for i in range(1, 11)]
print(f"1-10的平方：{squares}")

#10. 第三天打卡
print("=" * 30)
print("第三天打卡完成！")