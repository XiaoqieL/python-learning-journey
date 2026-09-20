dictl = {}
skipped = 0
for line in open("config.txt", "r", encoding="utf-8"):
    parts = line.split("=")
    if len(parts) != 2:
        skipped += 1
        print(f"Skipped:{skipped}")
        print(f"Skipped line: {line}")
        continue
    else:
        key = parts[0].strip()
        value = parts[1].strip()
        dictl[key] = value
print(f"成功解析 {len(dictl)} 条，跳过 {skipped} 条")
print("Day55 打卡完成！")