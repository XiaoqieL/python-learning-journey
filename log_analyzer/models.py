# ============ 日志分析系统 - 数据模型 ============

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass
class LogEntry:
    """单条日志记录"""
    timestamp: str
    level: str
    message: str
    source: Optional[str] = None

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "level": self.level,
            "message": self.message,
            "source": self.source or "",
        }


@dataclass
class AnalysisReport:
    """分析报告"""
    total_lines: int = 0
    level_counts: dict = field(default_factory=dict)
    error_messages: list = field(default_factory=list)
    top_errors: list = field(default_factory=list)
    time_range: tuple = ("", "")
    analysis_time: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
