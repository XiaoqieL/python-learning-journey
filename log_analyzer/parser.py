# ============ 日志分析系统 - 解析器 ============

import re
from collections import Counter
from models import LogEntry, AnalysisReport, LogLevel


class LogParser:
    """日志解析器"""

    # 匹配格式：2026-09-03 10:30:45 [ERROR] message here
    PATTERN = re.compile(
        r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s"
        r"$$(\w+)$$\s"
        r"(.+)"
    )

    def __init__(self):
        self.entries: list[LogEntry] = []

    def parse_line(self, line: str) -> LogEntry | None:
        """解析单行日志"""
        match = self.PATTERN.match(line.strip())
        if not match:
            return None
        return LogEntry(
            timestamp=match.group(1),
            level=match.group(2),
            message=match.group(3),
        )

    def parse_file(self, filename: str):
        """解析日志文件"""
        self.entries = []
        skipped = 0

        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            for line_num, line in enumerate(f, 1):
                entry = self.parse_line(line)
                if entry:
                    self.entries.append(entry)
                else:
                    skipped += 1

        print(f"解析完成：{len(self.entries)} 条有效, {skipped} 条跳过")
        return self.entries

    def analyze(self) -> AnalysisReport:
        """生成分析报告"""
        if not self.entries:
            print("没有日志数据分析")
            return AnalysisReport()

        # 1. 总行数
        total = len(self.entries)

        # 2. 按级别统计
        level_counter = Counter(e.level for e in self.entries)

        # 3. 收集所有ERROR和CRITICAL
        errors = [
            {"timestamp": e.timestamp, "level": e.level, "message": e.message}
            for e in self.entries
            if e.level in ["ERROR", "CRITICAL"]
        ]

        # 4. 统计错误消息频率TOP5

        error_msgs = [e.message for e in self.entries if e.level in ("ERROR", "CRITICAL")]
        top_errors = Counter(error_msgs).most_common(5)

        # 5. 时间范围
        timestamps = [e.timestamp for e in self.entries]
        time_range = (min(timestamps), max(timestamps))

        return AnalysisReport(
            total_lines=total,
            level_counts=dict(level_counter),
            error_messages=errors,
            top_errors=top_errors,
            time_range=time_range,
        )

    def filter_by_level(self, level: str) -> list[LogEntry]:
        """按级别过滤日志"""
        return [e for e in self.entries if e.level == level]

    def search_keyword(self, keyword: str) -> list[LogEntry]:
        """关键词搜索"""
        return [e for e in self.entries if keyword.lower() in e.message.lower()]

