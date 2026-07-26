# ============ 第二十三天：进制与位运算 ============

# ===== 1. 二进制基础 =====
print("===二进制基础===")

# Python中表示不同进制
num = 42
print(f"十进制：{num}")
print(f"二进制：{bin(num)}")  # 0b101010
print(f"八进制：{oct(num)}")  # 0o52
print(f"十六进制：{hex(num)}")  # 0x2a

# 不同进制转十进制
print(f"二进制101010转十进制：{int('101010', 2)}")  # 42
print(f"八进制52转十进制：{int('52', 8)}")  # 42
print(f"十六进制2a转十进制：{int('2a', 16)}")  # 42
print(f"十六进制FF转十进制：{int('FF', 16)}")  # 255

# ====== 2. 为什么程序要懂二进制? ======
print("\n=== 实际应用 ===")

# 存储单位换算(全都是2的冥次方)
print("1 KB = 1024 字节 = 2^10")
print("1 MB = 1024 MB = 2^20 字节")
print("1 GB = 1024 MB = 2^30 字节")
print(f"1GB = {2 ** 30} 字节")

# IP地址本质上就是32位二进制数
ip = "192.168.1.1"
parts = ip.split(".")
binary_ip = ".".join(bin(int(p)[2:].zfill(8)) for p in parts)
print(f"IP：{ip}")
print(f"二进制：{binary_ip}")

# 颜色也是十六进制
red = 0xFF0000
green = 0x00FF00
blue = 0x0000FF
print(f"\n红色：#{red:X}")
print(f"绿色：#{green:X}")
print(f"蓝色: #{blue:X}")

# ===== 3. 位运算 ====
print("\n=== 位运算 ===")

a = 12  # 二进制：1100
b = 10  # 二进制：1010

print(f"a = {a} = {bin(a)}")
print(f"b = {b} = {bin(b)}")

# 按位与AND：两位都为1才为1
print(f"a & b = {a & b} = {bin(a & b)}")  # 1000 = 8

# 按位或 OR、；只要有一位是1就是1
print(f"a | b = {a | b} = {bin(a | b)}")  # 1110 = 14

# 按位异或 XOR： 不同为1，相同为0
print(f"a ^ b = {a ^ b} = {bin(a ^ b)}")  # 0110 = 6

# 按位取反 NOT
print(f"~a    = {~a}")  # -(a+1) = -13

# 左移（乘以2的n次方）
print(f"a << 1 = {a << 1} = {bin(a << 1)}")  # 11000 = 24(乘2)
print(f"a << 2 = {a << 2} = {bin(a << 2)}")  # 110000 = 48(乘4)

# 右移（除以2的n次方， 向下取整）
print(f"a >> 1 = {a >> 1} = {bin(a >> 1)}")  # 110 = 6(除2）
print(f"a >> 2 = {a >> 2} = {bin(a >> 2)}")  # 11 = 3(除4）

# ===== 4. 位运算的实际用途 =====
print("\n=== 位运算的实战 ===")


# 用途1：判断奇偶（比 % 更快）
def is_odd(n):
    return n & 1 == 1


print(f"7是奇数：{is_odd(7)}")
print(f"8是奇数：{is_odd(8)}")

# 用途2：交换两个变量（不同第三个变量）
x, y = 10, 20
x = x ^ y
y = x ^ y
x = x ^ y
print(f"交换后：x={x}, y={y}")

# 用途3：权限系统（位掩码）
READ = 1  # 001
WRITE = 2 # 010
EXECUTE = 4 # 100

# 用户有读和执行权限
user_perms = READ | EXECUTE # 101 = 5
print(f"\n用户权限值：{user_perms}")
print(f"能否读：{bool(user_perms & READ)}")
print(f"能否写：{bool(user_perms & WRITE)}")
print(f"能否执行：{bool(user_perms & EXECUTE)}")

# 添加写权限
user_perms = user_perms | WRITE # 111 = 7
print(f"\n 添加写权限后: {user_perms}")
print(f"能否写: {bool(user_perms & WRITE)}")

# 移除执行权限
user_perms = user_perms & ~EXECUTE # 111 & 011 = 010
print(f"移除执行权限后：{user_perms}")
print(f"能否执行：{bool(user_perms & EXECUTE)}")

print("=" * 30)
print("第23天打卡完成！")