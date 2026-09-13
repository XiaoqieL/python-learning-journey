# ============ 日志分析系统 - 单元测试 ============
# 注意：在 log_analyzer 目录下运行，确保能 import parser


import pytest
from log_analyzer.parser import LogParser
from log_analyzer.models import AnalysisReport


@pytest.fixture
def parser():
    """每个测试都用一个全新的解析器"""
    return LogParser()


@pytest.fixture
def sample_entries():
    """构造一组测试用的日志"""
    lines = [
        "2026-09-03 10:30:45 [INFO] 服务启动成功",
        "2026-09-03 10:31:00 [ERROR] 数据库连接失败",
        "2026-09-03 10:31:30 [WARNING] 内存使用率80%",
        "2026-09-03 10:32:30 [CRITICAL] 服务不可用",
        "2026-09-03 10:33:30 [DEBUG] 缓存命中率",
        "2026-09-03 10:34:30 [INFO] 健康检查通过",
    ]
    return lines


class TestParseLine:
    """测试单行解析"""

    def test_valid_log(self, parser):
        """有效日志能正确解析"""
        entry = parser.parse_line("2026-09-03 10:30:45 [INFO] 服务启动成功")
        assert entry is not None
        assert entry.timestamp == "2026-09-03 10:30:45"
        assert entry.level == "INFO"
        assert entry.message == "服务启动成功"

    def test_error_level(self, parser):
        """能识别ERROR级别"""
        entry = parser.parse_line("2026-09-03 10:31:00 [ERROR] 数据库连接失败")
        assert entry.level == "ERROR"

    def test_critical_level(self, parser):
        """能识别CRITICAL级别"""
        entry = parser.parse_line("2026-09-03 10:32:30 [CRITICAL] 宕机")
        assert entry.level == "CRITICAL"

    def test_invalid_log(self, parser):
        """无效格式返回None"""
        assert parser.parse_line("不是日志格式的一行") is None
        assert parser.parse_line("") is None
        assert parser.parse_line("普通文字[没有时间]") is None

    def test_missing_bracket(self, parser):
        """缺方括号的日志无法解析"""
        assert parser.parse_line("2026-09-03 10:00:00 ERROR 没带括号") is None


class TestAnalyze:
    """测试统计分析"""

    def test_analyze_empty(self, parser):
        """能正确统计各级别数量"""
        for line in sample_entries:
            parser.entries.append(parser.parse_line(line))

        report = parser.analyze()
        assert report.total_lines == 7
        assert report.level_counts["INFO"] == 2
        assert report.level_counts["ERROR"] == 2
        assert report.level_counts["WARNING"] == 1
        assert report.level_counts["CRITICAL"] == 1
        assert report.level_counts["DEBUG"] == 1

    def test_error_message_collected(self, parser, sample_entries):
        """能收集所有错误日志"""
        for line in sample_entries:
            parser.entries.append(parser.parse_line(line))

        report = parser.analyze()
        # ERROR 2条 + CRITICAL 1条 = 3条错误级别
        assert len(report.error_messages) == 3
        # 所有收集的都是ERROR或CRRITICAL
        for err in report.error_messages:
            assert err["level"] in ["ERROR", "CRITICAL"]

    def test_top_errors(self, parser):
        """能正确统计错误TOP频率"""
        lines = [
            "2026-09-03 10:00:00 [ERROR] 重复错误",
            "2026-09-03 10:01:00 [ERROR] 重复错误",
            "2026-09-03 10:02:00 [CRITICAL] 重复错误",
            "2026-09-03 10:03:00 [ERROR] 其他错误",
        ]
        for line in lines:
            parser.entries.append(parser.parse_line(line))

        report = parser.analyze()
        assert report.top_errors[0][0] == "重复错误"
        assert report.top_errors[0][1] == 3


class TestSearchAndFilter:
    """测试搜索和过滤"""

    def test_filter_by_level(self, parser, sample_entries):
        """按级别过滤"""
        for line in sample_entries:
            parser.entries.append(parser.parse_line(line))

        errors = parser.filter_by_level("ERROR")
        assert len(errors) == 2
        for e in errors:
            assert e.level == "ERROR"

    def test_filter_no_match(self, parser):
        """过滤无匹配返回空列表"""
        assert parser.filter_by_level("ERROR") == []

    def test_search_keyword(self, parser, sample_entries):
        """能搜索包含关键词的日志"""
        for line in sample_entries:
            parser.entries.append(parser.parse_line(line))

        result = parser.search_keyword("数据库")
        assert len(result) == 1
        assert result[0].level == "ERROR"

    def test_search_case_insensitive(self, parser):
        """搜索不区分大小写"""
        parser.entries.append(parser.parse_line("2026-09-03 10:00:00 [INFO] Hello World"))
        result = parser.search_keyword("hello")
        assert len(result) == 1


class TestParserFile:
    """测试文件解析"""

    def test_parse_file(tmp_path):
        """能从文件读取并解析"""
        # tmp_path 是pytest提供的一个临时目录，测试结束自动清理
        log_file = tmp_path / "test.log"
        log_file.write_text(
            "2026-09-03 10:00:00 [INFO] 行1\n"
            "2026-09-03 10:01:00 [WARNING] 行2\n"
            "不是日志格式的行\n"   # 无效性，应跳过
            "2026-09-03 10:02:00 [ERROR] 行3\n",
            encoding="utf-8"
        )

        parser = LogParser()
        parser.parse_file(str(log_file))

        assert len(parser.entries) == 3  # 3条有效，1条无效跳过
        assert parser.entries[0].level == "INFO"
        assert parser.entries[-1].level == "ERROR"
