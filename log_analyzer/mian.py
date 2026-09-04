# ============ 日志分析系统 - 入口 ============

from log_analyzer.parser import LogParser
from models import AnalysisReport


def show_report(report: AnalysisReport):
    """打印分析报告"""
    print(f"\n{'=' * 55}")
    print(f" 日志分析报告")
    print(f"{'=' * 55}")
    print(f"  分析时间：{report.analysis_time}")
    print(f"  时间范围：{report.time_range[0]} ~ {report.time_range[1]}")
    print(f"  日志总数：{report.total_lines}")
    print(f"\n{'─' * 55}")
    print(f"  各级别统计:")
    print(f"{'─' * 55}")

    for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        count = report.level_counts.get(level, 0)
        pct = count / report.total_lines * 100 if report.total_lines else 0
        bar = "█" * int(pct / 2)
        print(f"  {level:<10} {bar} {count} ({pct:.1f}%)")

    if report.top_errors:
        print(f"\n{'─' * 55}")
        print(f"  错误TOP5:")
        print(f"{'─' * 55}")
        for i, (msg, count) in enumerate(report.top_errors, 1):
            print(f"  {i}. [{count}次] {msg[:50]}")

    if report.error_messages:
        print(f"\n{'─' * 55}")
        print(f"  最近5条错误日志:")
        print(f"{'─' * 55}")
        for err in report.error_messages[-5:]:
            print(f"  [{err['timestamp']}] {err['level']}: {err['message'][:50]}")

    print(f"\n{'=' * 50}")


def main():
    parser = LogParser()

    print(f"\n{'=' * 55}")
    print(f"  智能日志分析系统 v0.2")
    print(f"{'=' * 55}")

    while True:
        print(f"""
          1. 生成测试日志
          2. 解析日志文件
          3. 查看分析报告
          4. 按级别过滤
          5. 关键词搜索
          0. 退出
        """)
        choice = input("请选择：").strip()

        if choice == "1":
            from log_generator import generate_log
            count = int(input("生成条数（默认200）:") or "200")
            generate_log(count=count)

        elif choice == "2":
            filename = input("日志文件名(默认sample.log): ") or "sample.log"
            try:
                parser.parse_file(filename)
            except FileExistsError:
                print(f"文件不存在：{filename}, 请先生成测试日志")

        elif choice == "3":
            if not parser.entries:
                print("请先解析日志文件")
                continue
            report = parser.analyze()
            show_report(report)

        elif choice == "4":
            if not parser.entries:
                print("请先解析日志文件")
                continue
            level = input("级别(DEBUG/INFO/WARNING/ERROR/CRITICAL):").upper()
            results = parser.filter_by_level(level)
            print(f"\n找到{len(results)} 条 {level} 日志:")
            for e in results[:10]:
                print(f"   [{e.timestamp}] {e.message[:50]}")
            if len(results) > 10:
                print(f"    ...还有{len(results) - 10} 条")

        elif choice == "5":
            if not parser.entries:
                print("请先解析日志文件")
                continue
            keyword = input("搜索关键词：")
            results = parser.search_keyword(keyword)
            print(f" [{e.level}] [{e.timestamp}] {e.message[:50]}")

        elif choice == "0":
            print("再见！")
            break
        else:
            print("无效选择")


if __name__ == "__main__":
    main()
