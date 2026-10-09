def count_down(n):
    while n > 0:
        yield n
        n -= 1


for x in count_down(3):
    print(x)


# 输出3, 2, 1

def read_lines(filename):
    """逐行读文件，每次只占一行内容"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()  # 产出一行(去掉换行符)


# 用法：一行一行处理,不一次性全读
for line in read_lines("sample.log"):
    if "DEBUG" in line:
        print(line)
