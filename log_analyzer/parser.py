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

    def parse_file(self, filename: str):
        """解析日志文件"""
        # 明天实现
        pass

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

    def analyze(self) -> AnalysisReport:
        """生成分析报告"""
        # 明天实现
        pass
