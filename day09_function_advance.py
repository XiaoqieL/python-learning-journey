# ============ 第九天：函数进阶（加班精简）============

# 1. 多返回值
def calc(a, b):
    return a + b, a - b, a * b, a / b


add_r, sub_r, mul_r, div_r= calc(10, 3)
print(f"加：{add_r} 减：{sub_r} 乘：{mul_r} 除：{div_r}")


# 2. 可变参数 *args
def total(*nums):
    return sum(nums)


print(f"总和：{total(1, 2, 3, 4, 5)}")


# 3. 关键字参数 **kwargs
def info(**kw):
    for k, v in kw.items():
        print(f"{k}: {v}")


info(name="小茄", age=28, job="测试")

# 9. 第九天打卡
print("=" * 30)
print("第9天打卡完成！")
