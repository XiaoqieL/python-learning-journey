import os

if os.path.exists("sample.log"):  # 文件/文件夹存不存在 -> True/False
    print("sample.log 存在")
else:
    print("sample.log 不存在")

py_files = [f for f in os.listdir("D:\\git-learn") if f.endswith(".py")]  # 列出当前目录下所有文件名(列表)
print("git-learn 下的 .py文件:")
for f in py_files:
    print("-", f)

path = os.path.join("D:\\log", "断上电", "screenshot")
print("拼接的路径:", path)
if os.path.exists(path):
    print("该路径存在")
else:
    print("该路径不存在")
