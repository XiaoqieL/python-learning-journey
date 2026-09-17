i = "hello han"
count_dict = {}

for ch in i:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

for ch, cnt in count_dict.items():
    print(f"{ch}:{cnt}")
