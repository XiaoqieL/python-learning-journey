# ============ 第三十五天：全阶段复盘 ============
# 回顾你从 Day1 到 Day34 学了什么

review = {
    "阶段一 Python基础 （Day1-11）":[
        "Day1 变量、数据类型、print、f-string",
        "Day2 运算符、if/elif/else",
        "Day3 for循环、while循环",
        "Day4 列表 list(增删改查、切片)",
        "Day5 字符串（split/join/replace/正则）",
        "Day6 字典 dict",
        "Day7 元组 tuple、集合 set",
        "Day8 函数基础(def/参数/返回值)",
        "Day9 函数进阶(*args/**kwargs/多返回值)",
        "Day10 异常处理 try/except、文件IO",
        "Day11 面向对象 OOP（类/继承/封装）",
    ],
    "阶段二 Python进阶(Day12-22)":[
        "Day12 综合实战：待办事项管理器",
        "Day13 装饰器 decorator",
        "Day14 生成器 generator、迭代器 iterator",
        "Day15 上下文管理器 with/yield",
        "Day16 标准库(pathlib/datetime/json/re/logging)",
        "Day17 复习",
        "Day18 虚拟环境 venv、pip包管理",
        "Day19 pytest单元测试",
        "Day20 多线程/多进程",
        "Day21 模块化项目开发",
        "Day22 阶段复习",
    ],
    "阶段三 计算机底层(Day23-28)":[
        "Day23 进制转换、位运算",
        "Day24 内存模型(可变/不可变、深浅拷贝)",
        "Day25 网络协议（HTTP/TCP/UDP/状态码）",
        "Day26 数据库 SQLite CRUD",
        "Day27 爬虫基础(requests+BeautifulSoup)",
        "Day28 综合实战（爬取+清洗+存库+分析）",
    ],
    "阶段四 测试自动化(Day29-34)":[
        "Day29 requests接口测试入门",
        "Day30 pytest+requests接口框架",
        "Day31 pytest测试报告(HTML+标记)",
        "Day32 Playwright UI自动化",
        "Day33 完整测试项目(接口+UI+数据驱动)",
        "Day34 CI/CD持续集成",
    ],
}

print("=" * 50)
print("   35天学习复盘 - 你已经掌握了什么")
print("=" * 50)

total_skills = 0
for phase, items in review.items():
    print(f"\n{'─' * 50}")
    print(f"  {phase}")
    print(f"{'─' * 50}")
    for item in items:
        print(f"    ✓ {item}")
        total_skills += 1

print(f"\n{'=' * 50}")
print(f"  总计掌握 {total_skills} 个核心技能点！")
print(f"{'=' * 50}")

# 自我评估
print("\n📝 自我评估（1-5分）：")
skills = [
    "Python基础语法熟练度",
    "面向对象编程理解",
    "pytest测试框架掌握",
    "requests接口测试",
    "Playwright UI自动化",
    "数据库SQL操作",
    "CI/CD概念理解",
]
for i, skill in enumerate(skills, 1):
    print(f"  {i}. {skill}: ___分")

print(f"\n💡 接下来（Day36+）进入：综合项目实战")
print(f"   将用所学知识从零开发一个完整项目，放到GitHub作为作品集")
print(f"\n{'=' * 50}")
print("第35天打卡完成！")