# ============ 第十天：异常处理 ============

# 1. 为什么要异常处理
# 没有try 的写法---程序直接崩溃
# print(1/0) # ZeroDivisionError: division by zero

# 2. 基本结构：try / except
try:
    result = 1 / 0
except ZeroDivisionError:
    print("错误：除数不能为0")


# 3. 捕获多种异常

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("除数不能为0")
        return None
    except TypeError:
        print("请输入数字")
        return None


print(safe_divide(10, 3))
print(safe_divide(10, 0))


# 4. 捕获所有异常（不知道具体类型时使用)
def safe_get(dictionary, key):
    try:
        return dictionary[key]
    except Exception as e:
        print(f"出错了：{e}")
        return None


data = {"name": "小杰"}
print(safe_get(data, "name"))
print(safe_get(data, "age"))


# 5. try/ except / else / finally 完整结构
def read_number(text):
    try:
        num = int(text)
    except ValueError:
        print(f"'{text}' 不是有效数字")
    else:
        print(f"转换成功：{num}")
    finally:
        print("--- 处理完毕 ---")


read_number("42")
read_number("abc")


# ---- 举一反三练习区 ----
# 试试自己改：把上面的 safe_divide 加一个功能
# 如果结果大于10，打印"结果比较大"
def max_name(c):
    try:
        result1 = c
        if result1 > 10:
            print("结果比较大")
            return result1
    except ZeroDivisionError:
        print("错误：结果比较小")
        return None
    except TypeError:
        print("请输入这个数字")
        return None


print(max_name(10))
print(max_name(5))
print(max_name(20))
