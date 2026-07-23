# ============ 第二十一天：模块化项目实战 ============
# 学生成绩管理系统（模块化版）

import sys
from pathlib import Path

# 把当前目录加入搜索路径，确保能import
sys.path.insert(0, str(Path(__file__).parent))

from models.student import Student
from utils.file_helper import save_students, load_students
from utils.string_helper import extract_number, mask_phone, clean_text


def main():
    print("=" * 40)
    print("  学生管理系统 v2.0（模块化版）")
    print("=" * 40)

    # 1. 创建学生
    students = [
        Student("小杰", 28, 92),
        Student("李四", 25, 55),
        Student("王五", 27, 78),
        Student("赵六", 24, 88),
        Student("钱七", 26, 63),
    ]

    # 2. 显示所有学生
    print("\n--- 全部学生 ---")
    for s in students:
        print(s)

    # 3. 统计
    avg = sum(s.score for s in students) / len(students)
    top = max(students, key=lambda s: s.score)
    fail_count = sum(1 for s in students if s.score < 60)

    print(f"\n平均分：{avg:.1f}")
    print(f"最高分：{top.name} - {top.score}分")
    print(f"不及格人数：{fail_count}")

    # 4. 保存到文件
    save_students(students, "day21_students.json")

    # 5. 从文件读取
    print("\n--- 从文件读取 ---")
    data = load_students("day21_students.json")
    for item in data:
        print(f" {item['name']}: {item['score']}分 （{item['grade']}）")

    # 6. 测试字符串工具
    print("\n--- 字符串工具测试 ---")
    text = " 小杰的手机号是13812345678, QQ是123456 "
    print(f"原文：'{text}'")
    print(f"清理后：'{clean_text(text)}'")
    print(f"提取数字：{extract_number(text)}")
    print(f"手机脱敏：{mask_phone(text)}")

    print("\n" + "=" * 40)
    print("第21天打卡完成！")
    print("=" * 40)


if __name__ == '__main__':
    main()
