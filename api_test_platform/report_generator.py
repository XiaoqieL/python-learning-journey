# ============ HTML测试报告生成器 ============

import json
from datetime import datetime
from pathlib import Path
from db import Database


class ReportGenerator:
    """生成HTML测试报告"""

    def __init__(self, db: Database):
        self.db = db

    def generate(self, output_file="test_report.html"):
        """生成完整HTML报告"""
        results = self._get_all_results()

        passed = sum(1 for r in results if r["passed"])
        failed = len(results) - passed
        pass_rate = (passed / len(results) * 100) if results else 0
        avg_time = sum(r["response_time"] for r in results) / len(results) if results else 0

        html = self._build_html(results, passed, failed, pass_rate, avg_time)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ 报告已生成: {output_file}")
        return output_file

    def _get_all_results(self):
        cur = self.db.conn.execute(
            """
            SELECT * FROM test_results ORDER BY id DESC LIMIT 100
            """
        )
        return [dict(r) for r in cur.fetchall()]

    def _build_html(self, results, passed, failed, pass_rate, avg_time):
        rows_html = ""
        for r in results:
            status_class = 'pass' if r["passed"] else 'fail'
            status_text = "PASS" if r["passed"] else "FAIL"
            error = r["error_msg"] or "-"
            rows_html += f"""
             <tr class="{status_class}">
                <td>{r['id']}</td>
                <td>{r['case_name']}</td>
                <td><span class="badge">{status_text}</span></td>
                <td>{r['status_code']}</td>
                <td>{r['response_time']:.3f}s</td>
                <td>{error}</td>
                <td>{r['timestamp']}</td>
            </tr>"""

        total = len(results)
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""<!DOCTYPE html>     
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>API测试报告 - {now}</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Segoe UI', sans-serif; background: #f0f2f5; color: #333; padding: 20px; }}
.header {{ background: linear-gradient(135deg, #667eea, #764ba2); color: #fff;
           padding: 30px; border-radius: 12px; margin-bottom: 20px; }}
.header h1 {{ font-size: 28px; margin-bottom: 8px; }}
.header .meta {{ font-size: 14px; opacity: 0.9; }}
.summary {{ display: flex; gap: 16px; margin-bottom: 20px; }}
.card {{ flex: 1; background: #fff; padding: 24px; border-radius: 12px;
         text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
.card .num {{ font-size: 36px; font-weight: bold; }}
.card .label {{ color: #888; font-size: 14px; margin-top: 4px; }}
.card.total .num {{ color: #333; }}
.card.pass .num {{ color: #52c41a; }}
.card.fail .num {{ color: #ff4d4f; }}
.card.rate .num {{ color: #1890ff; }}
table {{ width: 100%; border-collapse: collapse; background: #fff;
        border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
th {{ background: #fafafa; padding: 14px; text-align: left; font-size: 13px;
      color: #666; border-bottom: 2px solid #f0f0f0; }}
td {{ padding: 12px 14px; border-bottom: 1px solid #f5f5f5; font-size: 14px; }}
tr.pass {{ background: #f6ffed; }}
tr.fail {{ background: #fff2f0; }}
.badge {{ display: inline-block; padding: 2px 10px; border-radius: 10px;
          font-size: 12px; font-weight: bold; }}
tr.pass .badge {{ background: #d9f7be; color: #389e0d; }}
tr.fail .badge {{ background: #ffccc7; color: #cf1322; }}
.footer {{ text-align: center; color: #999; margin-top: 20px; font-size: 13px; }}
</style>
</head>
<body>
<div class="header">
    <h1>API Test Report</h1>
    <div class="meta">生成时间: {now} | 用例总数: {total}</div>
</div>
<div class="summary">
    <div class="card total"><div class="num">{total}</div><div class="label">总用例</div></div>
    <div class="card pass"><div class="num">{passed}</div><div class="label">通过</div></div>
    <div class="card fail"><div class="num">{failed}</div><div class="label">失败</div></div>
    <div class="card rate"><div class="num">{pass_rate:.0f}%</div><div class="label">通过率</div></div>
</div>
<table>
<thead><tr>
    <th>ID</th><th>用例名称</th><th>结果</th><th>状态码</th>
    <th>响应时间</th><th>错误信息</th><th>执行时间</th>
</tr></thead>
<tbody>{rows_html}
</tbody></table>
<div class="footer">Powered by API Test Platform v0.3</div>
</body></html>"""
