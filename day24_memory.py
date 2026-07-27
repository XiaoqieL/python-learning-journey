# ============ 第二十四天：Python内存模型 ============

# ==== 1. 变量存在哪？======
print("==== 变量与内存 =====")


a = 100
b = 100
c = 1000

# id()查看内存地址
print(f"a的地址：{id(a)}")
print(f"b的地址：{id(b)}")
print(f"a和b是同一个对象：{a is b}")   # True ! 小整数Python会复用

print(f"c的地址：{id(c)}")
d = 1000
print(f"d的地址：{id(d)}")
print(f"c和d是同一个对象：{c is d}")  # False! 大整数Python不会复用

# ===== 2. 可变 vs 不可变类型 ====
print("\n==== 可变 vs 不可变 ====")

# 不可变：int,str,tuple----改了就创建新对象
x = 10
print(f"x地址：{id(x)}")
x = x + 1
print(f"x+1后地址：{id(x)}") # 地址变了，是新对象

# 可变：list,dict,set --- 原地改，地址不变
lst = [1, 2, 3]
print(f"lst地址：{id(lst)}")
lst.append(4)
print(f"append后地址：{id(lst)}")  # 地址没变,还是同一个对象


# ===== 3. 赋值的坑 ====
print("\n==== 赋值 vs 拷贝 ====")


# 坑：直接赋值是引用同一个对象
a_list = [1, 2, 3]
b_list = a_list
b_list.append(4)
print(f"a_list:{a_list}")  # [1, 2, 3, 4]---a也被改了！

# 正确：用copy()
import copy
c_list = a_list.copy()   # 浅拷贝
d_list = copy.deepcopy(a_list)  # 深拷贝
c_list.append(5)
print(f"a_list:{a_list}")    # [1, 2, 3, 4]--a没被改
print(f"c_list:{c_list}")    # [1, 2, 3, 4, 5]


# ===== 4. 浅拷贝 vs 深拷贝 ====
print("\n==== 浅拷贝 vs 深拷贝 ====")

original = [[1, 2], [3, 4]]

shallow = original.copy()    # 浅拷贝: 外层新对象，内层还是引用
shallow[0].append(999)
print(f"original:{original}") # [[1, 2, 999], [3, 4]]---被改了！

deep = copy.deepcopy(original) # 深拷贝: 完全独立的副本
deep[0].append(888)
print(f"original:{original}") #没变
print(f"deep:{deep}")        # [[1, 2, 999, 888], [3, 4]]


# ===== 5. 内存占用查看 ====
print("\n==== 内存占用查看 ====")


import sys
print(f"一个整数占：{sys.getsizeof(42)} 字节")
print(f"一个空列表占：{sys.getsizeof([])} 字节")
print(f"一个空字典占：{sys.getsizeof({})} 字节")
print(f"一个空字符串占：{sys.getsizeof('')} 字节")
print(f"一个空元组占：{sys.getsizeof(tuple())} 字节")
print(f"字符串'hello'占：{sys.getsizeof('hello')} 字节")

# ===== 6. Python内存管理：引用计数 ====
print("\n==== 引用计数 ====")

import gc

data = [1, 2, 3]
print(f"引用计数：{sys.getrefcount(data) - 1}") #减1因为getrefcount本身也引用了一次

# 当引用计数为0时，Python自动回收内存（垃圾回收）
del data # 删除引用
#print(data)  # NameError! 已经被回收了

print("del后变量不存在了，内存被自动回收")

print("=" * 30)
print("第24天打卡完成！")