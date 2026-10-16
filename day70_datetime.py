from datetime import datetime

a = datetime.now()
print(a)  # 拿当前时间 → 返回一个 datetime 对象

b = a.strftime("%Y-%m-%d %H:%M:%S")   # 时间 → 字符串（格式化输出）
print(b)


c = datetime.strptime("2026-10-06 20:00", "%Y-%m-%d %H:%M")  # 字符串 → 时间对象
print(c)
timedelta = a - c
print(timedelta)
print(timedelta.days)
print(timedelta.microseconds)
print(timedelta.seconds)