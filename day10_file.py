# ============ 第十天：文件IO ============

# 1. 写入文件
with open("day10_test.txt", "w", encoding="utf-8") as f:
    f.write("Python学习第10天\n")
    f.write("今天学了异常处理和文件IO\n")
    f.write("加油！\n")
print("写入成功")

# 2. 读取文件
with open("day10_test.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(f"文件内容：\n{content}")

# 3. 逐行读取
print("---逐行读取---")
with open("day10_test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"行：{line.strip()}")

# 4. 追加内容
with open("day10_test.txt", "a", encoding="utf-8") as f:
    f.write("这是追加的一行\n")
print("追加成功")

# 5. 实战：把列表写入文件
students = ["张三,90", "李四,85", "王五,78"]
with open("day10_students.txt", "w", encoding="utf-8") as f:
    for s in students:
        f.write(s + "\n")
print("学生数据写入成功")

# 6. 实战：读取文件并处理（dict和异常）
scores = {}
with open("day10_students.txt", "r", encoding="utf-8") as f:
    for line in f:
        try:
            name, score = line.strip().split(",")
            scores[name] = int(score)
        except ValueError:
            continue
print(f"成绩数据：{scores}")

# 找最高分
best = max(scores, key=scores.get)
print(f"最高分：{best} - {scores[best]}分")

# --- 举一反三练习区 ---
# 试试自己改：再往students列表中添加数据，并把数据写入文件
