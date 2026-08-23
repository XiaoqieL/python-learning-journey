# ============ API测试执行引擎 ============

import requests
import time
import json
from models import TestCase, TestResult
from db import Database


class APITester:
    """接口测试执行引擎"""

    def __init__(self, db: Database):
        self.db = db
        self.results = []

    def run_case(self, case: TestCase):
        """执行单个测试用例"""
        print(f" 执行：{case.name} [{case.method}] {case.url}")

        result = TestResult(
            case_id=case.id,
            case_name=case.name,
            passed=False,
            status_code=0,
            response_time=0.0,
        )

        try:
            start = time.time()
            if case.method == "GET":
                resp = requests.get(case.url, headers=case.headers, timeout=10)
            elif case.method == "POST":
                resp = requests.post(case.url, json=case.body, headers=case.headers, timeout=10)
            elif case.method == "PUT":
                resp = requests.put(case.url, json=case.body, headers=case.headers, timeout=10)
            elif case.method == "DELETE":
                resp = requests.delete(case.url, headers=case.headers, timeout=10)
            else:
                result.error_msg = f"不支持的方法：{case.method}"
                return result

            elapsed = time.time() - start
            result.status_code = resp.status_code
            result.response_time = elapsed

            # 断言1：状态码
            status_ok = (resp.status_code == case.expected_status)

            # 断言2：字段值（如果配置了）
            field_ok = True
            if case.expected_field:
                try:
                    data = resp.json()
                    actual_value = data.get(case.expected_field)
                    field_ok = (str(actual_value) == str(case.expected_value))
                    if not field_ok:
                        result.error_msg = f"字段{case.expected_field}期望={case.expected_value} 实际={actual_value}"
                except Exception:
                    field_ok = False
                    result.error_msg = "响应不是JSON格式"

            result.passed = status_ok and field_ok
            status_str = "✓ PASS" if result.passed else "✗ FAIL"
            print(f"    → {status_str} 状态码:{resp.status_code} 耗时:{elapsed:.3f}秒")
            if not result.passed and not result.error_msg:
                result.error_msg = f"状态码不匹配：期望{case.expected_status}, 实际：{resp.status_code}"

        except requests.exceptions.Timeout:
            result.error_msg = "请求超时"
            print(f"    → ✗ FAIL 超时")
        except requests.exceptions.ConnectionError:
            result.error_msg = "连接失败"
            print(f"    → ✗ FAIL 连接失败")
        except Exception as e:
            result.error_msg = str(e)
            print(f"    → ✗ FAIL {e}")

        # 存结果
        self.db.save_result(result)
        self.results.append(result)
        return result

    def run_all(self):
        """执行所有测试用例"""
        cases = self.db.get_all_cases()
        if not cases:
            print("暂无测试用例，请先添加！")
            return []

        print(f"\n{'=' * 60}")
        print(f"  开始执行 {len(cases)} 条测试用例")
        print(f"{'=' * 60}\n")

        passed = 0
        failed = 0
        for i, case in enumerate(cases, 1):
            print(f"{i}/{len(cases)}", end="")
            result = self.run_case(case)
            if result.passed:
                passed += 1
            else:
                failed += 1

        print(f"\n{'=' * 60}")
        print(f"  执行完毕: {passed} 通过, {failed} 失败, 共 {len(cases)} 条")
        print(f"  通过率: {passed / len(cases) * 100:.0f}%")
        print(f"{'=' * 60}")

        return self.results

    def get_history(self, limit=20):
        """查询历史结果"""
        cur = self.db.conn.execute(
            "SELECT * FROM test_results ORDER BY id DESC LIMIT ?", (limit,)
        )
        rows = cur.fetchall()
        if not rows:
            print("暂无历史记录")
            return []
        print(f"\n{'ID':<5} {'用例':<20} {'结果':<8} {'状态码':<8} {'耗时':<10} {'时间'}")
        print("-" * 70)
        history = []
        for r in rows:
            status = "✓ PASS" if r["passed"] else "✗ FAIL"
            print(
                f"{r['id']:<5} {r['case_name']:<20} {status:<8} {r['status_code']:<8} {r['response_time']:.3f}s{'':<4} {r['timestamp']}")
            history.append(dict(r))
        return history
