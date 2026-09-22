dica = {}

while True:
    name = input("请输入姓名: ").strip()
    if name == "q":
        break
    score = int(input("请输入分数: "))
    dica[name] = score

[print(f"{name}的分数是{score}") for name, score in dica.items() if score < 60]
print(f"总共分数为{sum(dica.values())}")
print(f"平均分数为{sum(dica.values()) / len(dica)}")
print(f"最高分是{max(dica.values())}")
print(f"最低分是{min(dica.values())}")
print(dica)
