# ============ 第二十八天：综合实战 - 爬取+清洗+存库 ============

import requests
from bs4 import BeautifulSoup
import sqlite3
import json
import re
import csv
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


# ===== 第1步：爬取数据（如果网络不通用模拟数据）=====
def fetch_data():
    """爬取数据，网络不通时返回模拟数据"""
    print("[1/5]正在爬取数据...")

    # 模拟爬取的结果（结构和真是爬出来的一样）
    # 实际工作中，这里会用requests.get + BeautifulSoup 抓网页
    raw_date = [
        {"title": " Python入门教程  ", "author": "  张三 ", "price": "¥299元", "date": "2026/07/01",
         "url": "https://example.com/1"},
        {"title": "爬虫实战指南!", "author": "李四", "price": "399", "date": "2026-07-15", "url": "https://example.com/2"},
        {"title": "   数据库原理与实践   ", "author": "王五", "price": "¥199", "date": "2026.06.20",
         "url": "https://example.com/3"},
        {"title": "算法与数据结构", "author": "赵六  ", "price": "499元", "date": "2026/08/01", "url": "https://example.com/4"},
        {"title": "网络协议详解", "author": "钱七", "price": "¥259", "date": "2026-07-28", "url": "https://example.com/5"},
        {"title": "测试自动化完整教程", "author": " 孙八", "price": "359", "date": "2026.07.10", "url": "https://example.com/6"},
        {"title": "面向对象设计模式", "author": "周九", "price": "¥449元", "date": "2026/06/25", "url": "https://example.com/7"},
        {"title": "Git版本控制实战", "author": "吴十", "price": "99", "date": "2026-07-05", "url": "https://example.com/8"},
        {"title": "   数据结构与算法", "author": "郑十一 ", "price": "¥399", "date": "2026.07.20",
         "url": "https://example.com/9"},
        {"title": "并发编程", "author": "王十二", "price": "¥299", "date": "2026/07/12", "url": "https://example.com/10"},
    ]
    print(f"   爬取到{len(raw_date)} 条原始数据")
    return raw_date


# ===== 第2步：数据清洗（脏数据 → 干净数据）=====
def clean_data(raw_list):
    """清洗原始数据：去空格、统一格式、转类型"""
    print("[2/5] 正在清洗数据...")

    cleaned = []
    for item in raw_list:
        # 1. 去首尾空格
        title = item["title"].strip()
        author = item["author"].strip()

        # 2. 统一价格：提取数字，转成flot
        price_str = item["price"]
        price_num = float(re.sub(r"[^\d]", "", price_str))  # 去掉非数字和小数点

        # 3. 统一日期格式：全部转成 YYYY-MM-DD
        date_str = item["date"]
        date_clean = re.sub(r"[/.]", "-", date_str)
        try:
            date_obj = datetime.strptime(date_clean, "%Y-%m-%d")
        except ValueError:
            date_obj = datetime.now()
        date_standard = date_obj.strftime("%Y-%m-%d")

        # 4. 标题规范化：去掉特殊字符，首字母大写
        title_clean = re.sub(r"[!！？?.。]+$", "", title)

        cleaned.append({
            "title": title_clean,
            "author": author,
            "price": price_num,
            "publish_date": date_standard,
            "url": item["url"],
            "crawl_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # 5. 去重(按title+author)
    seen = set()
    unique = []
    for item in cleaned:
        key = (item["title"], item["author"])
        if key not in seen:
            seen.add(key)
            unique.append(item)

    print(f"  清洗后剩余{len(unique)} 条(去重后)")
    return unique


# ===== 第3步：存入数据库 =====
def save_to_db(data, db_file="day_28_course.db"):
    """数据存入SQLite"""
    print("[3/5] 正在保存数据到数据库...")

    if Path(db_file).exists():
        Path(db_file).unlink()

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE courses (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        title        TEXT    NOT NULL,
        author       TEXT,
        price        REAL,
        publish_date TEXT,
        url          TEXT,
        crawl_time   TEXT
    )
    """)

    # 批量插入
    cur.executemany("""
        INSERT INTO courses(title, author, price, publish_date, url, crawl_time)
        VALUES (:title, :author, :price, :publish_date, "url, :crawl_time)
    """, data)
    conn.commit()

    # 验证
    cur.execute("SELECT COUNT(*) FROM courses")
    cnt = cur.fetchone()[0]
    conn.close()
    print(f"   数据库中已保存{cnt} 条记录")


# ===== 第4步：导出CSV + JSON =====
def export_files(data):
    """导出CSV和JSON两种格式"""
    print("[4/5] 正在导出数据...")

    # CSV
    csv_path = "day28_courses.csv"
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerow(data)
    print(f"   CSV已导出：{csv_path}")

    # JSON
    json_path = "day28_courses.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"    JSON已导出：{json_path}")


# ==== 第5步：统计分析 =====
def analyze(db_file="day28_courses.db"):
    """从数据库读取并做统计分析"""
    print("[5/5] 正在统计分析...\n")

    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    print("======= 数据报告=====")

    # 总数
    cur.execute("SELECT COUNT(*), AVG(price), MAX(price), MIN(price) FROM courses")
    total, avg_p, max_p, min_p = cur.fetchone()
    print(f"课程总数：{total}")
    print(f"平均价格：¥{avg_p:.2f}")
    print(f"最高价格：¥{max_p:.2f}")
    print(f"最低价格：¥{min_p:.2f}\n")

    # 按价格区间统计
    cur.execute("""
        SELECT
           CASE 
                WHEN price < 200 THEN '¥0-200'
                WHEN price < 300 THEN '¥200-300'
                WHEN price < 400 THEN '¥300-400'
                ELSE '¥400+'
           END AS price_range,
           COUNT(*) AS cnt
        FROM courses GROUP BY price_range ORDER BY price_range
    """)
    print("价格区间分布：")
    for row in cur.fetchall():
        bar = "█" * row["cnt"]
        print(f"   {row['price_range']:>8} | {bar} {row['cnt']}门")

    # 按月份统计
    cur.execute("""
         SELECT substr(publish_date, 1, 7) AS month, COUNT(*) AS cnt
        FROM courses GROUP BY month ORDER BY month
    """)
    print("\n按月发布数量：")
    for row in cur.fetchall():
        bar = "█" * row["cnt"]
        print(f"  {row['month']} | {bar} {row['cnt']}门")

    # 最贵的3门课
    cur.execute("SELECT title, author, price FROM courses ORDER BY price DESC LIMIT 3")
    print("\nTOP3 最贵课程：")
    for i, row in enumerate(cur.fetchall(), 1):
        print(f"  {i}. {row['title']} - {row['author']} ¥{row['price']:.0f}")

    # 2026年7月之后的课程
    cur.execute("""
         SELECT title, publish_date FROM courses 
        WHERE publish_date >= '2026-07-01' 
        ORDER BY publish_date DESC
    """)
    print("\n7月后新发布课程：")
    for row in cur.fetchall():
        print(f"  [{row['publish_date']}] {row['title']}")

    conn.close()
    print("\n======== 分析完成 ========")


# ===== 主流程 =====
def main():
    print("=" * 50)
    print("   综合实战：爬取 → 清洗 → 存库 → 导出 → 分析")
    print("=" * 50 + "\n")

    raw = fetch_data()  # 1.爬取
    clean = clean_data(raw)  # 2.清洗
    save_to_db(clean)  # 3.存库
    export_files(clean)  # 4.导出
    analyze()  # 5.分析

    print("\n" + "=" * 50)
    print("第28天打卡完成！")
    print("爬虫+清洗+数据库+导出+分析 全流程搞定！")
    print("=" * 50)


if __name__ == "__main__":
    main()
