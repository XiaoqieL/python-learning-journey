# ============ 日志分析系统 - 入口 ============

from log_analyzer.parser import LogParser


def mian():
    print("=" * 50)
    print("  智能日志分析系统 v0.1")
    print("=" * 50)
    print("  今天搭骨架，明天写解析器")
    print("  功能：解析日志 → 统计 → 报告")
    print("=" * 50)

    # 测试解析器能否识别日志格式
    parser = LogParser()

    test_lines = [
        "2026-09-03 10:30:45 [ERROR] 数据库连接失败",
        "2026-09-03 10:31:00 [INFO] 服务启动成功",
        "2026-09-03 10:31:30 [WARNING] 内存使用率80%",
        "2026-09-03 10:32:00 [ERROR] 接口超时",
    ]

    print("\n--- 测试日志解析 ---")
    for line in test_lines:
        entry = parser.parse_line(line)
        if entry:
            print(f" ✓ [{entry.level}] {entry.timestamp} → {entry.message}")
        else:
            print(f" ✗ 无法解析：{line}")

    print("\n骨架搭建完成! 明天实现文件解析和统计。")


if __name__ == "__main__":
    mian()
