# ============ API测试管理平台 - 入口 ============

import sys
from db import Database
from api_tester import APITester


def show_menu():
    print("""
╔══════════════════════════════════╗
║    API 测试管理平台 v0.3           ║
╠══════════════════════════════════╣
║  1. 添加测试用例                   ║
║  2. 查看所有用例                   ║
║  3. 执行所有测试                   ║
║  4. 查看历史结果                   ║
║  5. 生成测试报告                   ║
║  0. 退出                          ║
╚══════════════════════════════════╝
    """)


# 选项5的实现
def generate_report(db):
    from report_generator import ReportGenerator
    rg = ReportGenerator(db)
    rg.generate("test_report.html")


def add_case(db):
    from models import TestCase
    print("\n--- 添加测试用例 ---")
    name = input("用例名称：")
    method = input("请求方法(GET/POST)：").upper() or "GET"
    url = input("请求URL：")
    expected_status = int(input("期望状态码（默认为200）") or "200")

    body = None
    if method == "POST":
        body_str = input("请求JSON（可留空）:")
        if body_str:
            try:
                body = eval(body_str)
            except:
                body = None

    case = TestCase(name=name, method=method, url=url, expected_status=expected_status, body=body)
    case_id, msg = db.add_case(case)
    if case_id:
        print(f"✓ 添加成功，ID={case_id}")
    else:
        print(f"✗ 添加失败: {msg}")


def list_cases(db):
    case = db.get_all_cases()
    if not case:
        print("暂无用例")
        return
    print(f"\n{'ID':<5} {'名称':<20} {'方法':<8} {'URL':40} {'期望状态'}")
    print("-" * 80)
    for c in case:
        print(f"{c.id:<5} {c.name:<20} {c.method:<8} {c.url[:38]:<40} {c.expected_status}")


def run_tests(db):
    tester = APITester(db)
    tester.run_all()


def show_history(db):
    tester = APITester(db)
    tester.get_history()


def main():
    db = Database()
    while True:
        show_menu()
        choice = input("请选择：").strip()
        if choice == "1":
            add_case(db)
        elif choice == "2":
            list_cases(db)
        elif choice == "3":
            run_tests(db)
        elif choice == "4":
            show_history(db)
        elif choice == "5":
            generate_report(db)
        elif choice == "0":
            db.close()
            print("再见！")
            break
        else:
            print("无效选择")


if __name__ == "__main__":
    main()
