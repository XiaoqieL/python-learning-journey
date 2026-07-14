# ============ 第十二天：综合实战 - 待办事项管理器 ============

import os


class TodoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.todos = []
        self.load()

    def _load(self):
        """从文件加载"""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        done, text = line.strip().split("|", 1)
                        self.todos.append({"text": text, "done": done == "V"})
                    except ValueError:
                        continue

    def add(self, text):
        self.todos.append({"text": text, "done": False})
        print(f"添加：{text}")

    def done(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]["done"] = True
            print(f"完成：{self.todos[index]['text']}")

    def show(self):
        print("\n===== 待办清单 =====")
        if not self.todos:
            print("（空）")
            return
        for i, item in enumerate(self.todos):
            status = "V" if item["done"] else " "
            print(f"[{status}] {i}. {item['text']}")
        print('=============\n')

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for item in self.todos:
                mark = "V" if item["done"] else " "
                f.write(f"{mark}|{item['text']}\n")
        print(f"已保存到 {self.filename}")


# 使用
todo = TodoList()
todo.show()

todo.add("学习 Python第12天")
todo.add("复习OOP")
todo.add("把代码推到GitHub")

todo.done(0)
todo.show()

todo.save()
