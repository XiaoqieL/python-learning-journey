# ============ 数据模型 ============

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class TestCase:
    """测试用例模型"""
    id: Optional[int] = None
    name: str = ""
    method: str = "GET"  # GET/POST/PUT/DELETE
    url: str = ""
    headers: dict = field(default_factory=dict)
    body: Optional[dict] = None
    expected_status: int = 200
    expected_field: Optional[str] = None
    expected_value: Optional[str] = None

    def validate(self):
        if not self.name:
            return False, "用例名不能为空"
        if not self.url:
            return False, "URL不能为空"
        if self.method not in ("GET", "POST", "PUT", "DELETE"):
            return False, "请求方法只能是GET/POST/PUT/DELETE"
        return True, "OK"


@dataclass
class TestResult:
    """测试结果模型"""
    case_id: int
    case_name: str
    passed: bool
    status_code: int
    response_time: float
    error_msg: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def to_dict(self):
        return {
            "case_id": self.case_id,
            "case_name": self.case_name,
            "passed": self.passed,
            "status_code": self.status_code,
            "response_time": round(self.response_time, 3),
            "error_msg": self.error_msg,
            "timestamp": self.timestamp,
        }
