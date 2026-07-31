# ============ 第二十六天：数据库SQLite基础 ============
# SQLite 是 Python 内置的，不用安装，直接用！
# MySQL 语法几乎一样，后面换 MySQL 只改连接就行。

import sqlite3
from pathlib import Path

# ===== 1. 连接数据库 =====
db_path = Path("day26_students.db")
if db_path.exists():
    db_path.unlink()  # 清理旧数据，保证每次运行结果一致

conn = sqlite3.connect(str(db_path))
cursor = conn.cursor()
print("数据库连接成功")

# ===== 2. 创建表 =====
cursor.execute("""
CREATE TABLE students(
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT    NOT NULL,
    age   INTEGER,
    score REAL,
    grade TEXT
)
""")
conn.commit()
print("students 表创建成功")

# ===== 3. 插入数据（C - Create）======
print("\n==== 插入数据=====")

# 单条插入
cursor.execute("INSERT INTO students(name, age, score, grade) VALUES (?, ?, ?, ?)",
               ("小杰", 28, 92.5, "优秀"))

conn.commit()
print(f"插入1条, 最新ID：{cursor.lastrowid}")

# 批量插入(比循环单条快很多)
students_data = [
    ("李四", 25, 55.0, "不及格"),
    ("王五", 27, 78.5, "及格"),
    ("赵六", 24, 88.0, "良好"),
    ("钱七", 26, 63.5, "及格"),
    ("孙八", 29, 95.0, "优秀"),
    ("周九", 23, 48.0, "不及格"),
]
cursor.executemany(
    "INSERT INTO students(name, age, score, grade) VALUES (?, ?, ?, ?)",
    students_data
)
conn.commit()
print(f"批量插入 {len(students_data)} 条完成")

# ===== 4. 查询数据（R - Read）======
print("\n==== 查询数据=====")

# 查全部
cursor.execute("SELECT * FROM students")
all_rows = cursor.fetchall()
print(f"\n全部学生（共{len(all_rows)}条）：")
for row in all_rows:
    print(f"  {row}")

# 按条件查询
cursor.execute("SELECT name, score FROM students WHERE score >= 80 ORDER BY score DESC")
good_students = cursor.fetchall()
print(f"\n80分以上(按分数降序)：")
for name, score in good_students:
    print(f"   {name}: {score}")

# 查一条
cursor.execute("SELECT * FROM students WHERE name = ?", ("小杰",))
one = cursor.fetchall()
print(f"\n查单个-小杰：{one}")

# 统计
cursor.execute("SELECT COUNT(*), AVG(score), MAX(score), MIN(score) FROM students")
cnt, avg_s, max_s, min_s = cursor.fetchone()
print(f"\n统计：总人数={cnt}, 平均分={avg_s:.1f} 最高={max_s} 最低={min_s}")

# 分组统计
cursor.execute("SELECT grade, COUNT(*) FROM students GROUP BY grade ORDER BY grade")
print(f"\n按等级分组：")
for grade, count in cursor.fetchall():
    print(f"  {grade}: {count}人")

# ===== 5. 更新数据（U - Update）======
print("\n==== 更新数据=====")
cursor.execute("UPDATE students SET score = ?, grade = ? WHERE name = ?",
               (90.0, "良好", "钱七"))
conn.commit()
print(f"钱七的分数已更新为85分(影响{cursor.rowcount}行)")

cursor.execute("SELECT name, score, grade FROM students WHERE name = '钱七")
print(f"验证结果：{cursor.fetchall()}")

# ===== 6. 删除数据（D - Delete）======
print("\n==== 删除数据=====")
cursor.execute("DELETE FROM student WHERE score < 60")
conn.commit()
print(f"删除不及格学生(影响{cursor.rowcount}行)")

cursor.execute("SELECT COUNT(*) FROM students")
print(f"剩余学生数：{cursor.fetchone()[0]}")

# ====== 7. 实战：用Python面向对象操作数据库 ======
print("\n ==== 实战：学生管理DB类====")


class StudentDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.conn.row_factory = sqlite3.Row  # 让结果支持字段名访问
        self.cur = self.conn.cursor()

    def add(self, naem, age, score):
        grade = self._calc_grade(score)
        self.cur.execute(
            "INSERT INIO students (name, age, score, grade) VALUES(?,?,?,?)",
            (name, age, score, grade))
        self.conn.commit()
        return self.cur.lastrowid

    def list_all(self):
        self.cur.execute("SELECT * FROM students ORDER BY score DESC")
        return [dict(r) for r in self.cur.fetchall()]

    def search(self, name):
        self.cur.execute("SELECT * FROM students WHERE name = LIKE ?", (f"%{name}%",))
        return [dict(r) for r in self.cur.fetchall()]

    def _calc_grade(self, score):
        if score >= 90:
            return "优秀"
        elif score >= 80:
            return "良好"
        elif score >= 60:
            return "及格"
        else:
            return "不及格"

    def close(self):
        self.conn.close()


# 使用
db = StudentDB(str(db_path))
db.add("武士", 30, 91.0)
db.add("郑十一", 22, 72.0)

print(f"\n全部学生（按分数排序）：")
for s in db.list_all():
    print(f"   [{s['id']}] {s['name']}({s['age']}岁){s['score']:.1f}分 {s['grade']}")

print("\n搜索'王'：")
for s in db.search("王"):
    print(f"  {s['name']}: {s['score']}分")

db.close()
conn.close()

print("\n" + "=" * 30)
print("第26天打卡完成！CRUD + 数据库实战全部搞定！")
