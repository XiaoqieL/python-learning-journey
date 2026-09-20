import json, os

records = {}  # 记账字典
FILE = "account.json"

if os.path.exists(FILE):
    records = json.load(open(FILE, encoding="utf-8"))

while True:
    print("\n1.记一笔账 2.查看 3.总支出 4.删除记录 0.退出")
    choice = input("请选择: ")
    if choice == "1":
        name = input("请输入姓名: ").strip()
        try:
            amount = float(input("金额: "))
        except ValueError:
            print("金额必须是数字!")
            continue
        records[name] = records.get(name, 0) + amount
    elif choice == "2":
        for k, v in records.items():
            print(f"{k} ¥{v:.2f}")
    elif choice == "3":
        print(f"总支出: ¥{sum(records.values()):.2f}")
    elif choice == "4":
        name = input("请输入姓名：").strip()
        if name in records:
            del records[name]
            print(f"已删除{name}的记录")
            continue
        else:
            print(f"{name}没有记录")
    elif choice == "0":
        json.dump(records, open(FILE, "w", encoding="utf-8"), ensure_ascii=False)
        print("已保存账单")
        break
    else:
        print("无效的选择")




