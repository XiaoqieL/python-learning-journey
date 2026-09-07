# ============ 日志分析系统 - HTML报告生成器 ============

from datetime import datetime
from pathlib import Path
from models import AnalysisReport


class ReportGenerator:
    """生成可视化HTML报告"""

    LEVEL_COLORS = {
        "DEBUG": "#999",
        "INFO": "#1890ff",
        "WARNING": "#faad14",
        "ERROR": "#ff4d4f",
        "CRITICAL": "#cf1322",
    }

    def generate(self, report: AnalysisReport, output="log_report.html"):
        """生成完整HTML报告"""
        html = self._build_html(report)
        Path(output).write_text(html, encoding="utf-8")
        print(f"✓ 报告已生成: {output}")
        return output

    def _build_html(self, r: AnalysisReport):
        # 级别统计柱状图
        level_bar = ""
        for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            count = r.level_counts.get(level, 0)
            pct = count / r.total_lines * 100 if r.total_lines else 0
            color = self.LEVEL_COLORS.get(level, "#999")
            bar_width = int(pct * 3)
            level_bar += f"""
            <div class="level-row">
                 <span class="level-label" style="color:{color}">{level}</span>
                 <div class="bar-container">
                      <div class="bar-fil" style="width:{pct}%,background:{color}"></div>
                 </div>
                 <span class="level-count">{count} ({pct:.1f}%)</span>
            </div>"""

        # 错误TOP5表格
        top_error_rows = ""
        if r.top_errors:
            for i, (msg, count) in enumerate(r.top_errors, 1):
                top_error_rows += f"""
                 <tr>
                   <td>{i}</td>
                   <td>{msg[:60]}</td>
                   <td><span class="error-count">{count}</span></td>
                 </tr>"""
        else:
            top_error_rows = '<tr><td colspan="3" style="text-align:center;color:#999">无错误记录</td></tr>'

        # 最近错误日志
        recent_errors = ""
        if r.error_messages:
            for err in r.error_messages[-10:]:
                recent_errors += f"""
                <tr class="{err['level'].lower()}">
                    <td>{err['timestamp']}</td>
                    <td><span class="badge {err['level'].lower()}">{err['level']}</span></td>
                    <td>{err['message']}</td>
                </tr>"""
        else:
            recent_errors = '<tr><td colspan="3" style="text-align:center;color:#999">五=无错误日志</td></tr>'

        total = r.total_lines
        error_count = r.level_counts.get("ERROR", 0) + r.level_counts.get("CRITICAL", 0)
        error_rate = error_count / total * 100 if total else 0
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>日志分析报告 - {now}</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body{{ font-family: 'Segoe UI', sans-serif; background: #f0f2f5; color: #333; padding: 20px; }}
.header {{ background: liner-gradient(135deg, #557eea, #764ba2); color: #fff;
           padding: 30px; border-radius: 12px; margin-bottom: 20px; }}
.header h1 {{ font-size: 26px; margin-bottom: 8px; }}
.header .meta {{ font-size: 13px; opacity: 0.9; }}
.summary {{ display: flex; gap: 16px; margin-bottom: 20px; }}
.card {{ flex: 1; background: #fff; padding: 24px; border-radius: 12px; 
          text-align: center; box-shadow:0 2px 8px rgba(0,0,0,0.08);}}
.card .num{{ font-size: 32px; font-weight: bold; }}
.card .label{{ color: #888; font-size: 13px; margin-top: 4px; }}
.card.total .num {{ color: #333; }}
.card.errors .num {{ color: #ff4d4f; }}
.card.rate .num {{ color: #faad14; }}
.card.range .num {{ font-size: 14px; color: #1890ff; }}
.section {{ background: #fff; padding: 24px; border-radius: 12px;
            margin-bottom: 20px; box-shadow:0 2px 8px rgba(0,0,0,0.08); }}
.section h2 {{ font-size: 18px; margin-bottom: 16px; color: #333; }}
.level-row {{ display: flex; align-items: center; margin-bottom:  12px; }}
.level-label {{ width: 80px; font-weight: bold; font-size: 14px; }}
.bar-container {{ flex: 1; height: 24px; background: #f0f0f0; 
                  border-radius: 12px; overflow: hidden; margin: 0 12px; }}
.bar-fill {{ height: 100%; border-redius: 12px; transition: width 0.5s; }}
.level-count {{ width: 120px; font-size: 13px; color: #666; }}
table {{ width: 100%; border-collapse: collapse; }}
th {{ background: #fafafa; padding: 12px; text-align: left; font-size: 13px;
      color: #666; border-bottom: 2px solid #f0f0f0; }}
td {{ padding: 10px 12px; border-bottom: 1px solid #f5f5f5; font-size: 14px;}}
tr.error {{ background: #fff2f0; }}
tr.critical {{ background: #fff1f0; }}
.badge {{ display: inline-block; padding: 2px 10px; border-radius: 10px;
          font-size: 12px; font-weight: bold; }}
.badge.error {{ background: #ffccc7; color: #cf1322; }}
.badge.critical {{ background: #ffa39e; color: #cf1322; }} 
.badge.warning {{ background: #ffe58f; color: #d48806; }}
.badge.info {{ background: #bde4ff; color: #1890ff;}}
.badge.debug {{ background: #f0f0f0; color: #999; }}
.error-count {{ font-weight: bold; color: #ff4d4f; }}
.footer {{ text-align: center; color: #999; margin-top: 20px; font-size: 13px;}}
</style>
</head>
<body>
<div class="header">
     <h1>Log Analysis Report</h1>
     <div class="meta">生成时间: {now} | 日志总数：{total} | 时间范围：{r.time_range[0]} ~ {r.time_range[1]}</div>
</div>
<div class="summary">
     <div class="card total"><div class="num">{total}</div><div class="label">日志总数</div></div>
     <div class="card errors"><div class="num">{error_count}</div><div class="label">错误总数</div></div>
    <div class="card rate"><div class="num">{error_rate:.1f}%</div><div class="label">错误率</div></div>
    <div class="card range"><div class="num">{r.time_range[0][5:]}~{r.time_range[1][5:]}</div><div class="label">时间范围</div></div>
</div>
<div class="section">
      <h2>各级别分布</h2>
      {level_bar}
</div>
<div class="section">
     <h2>错误TOP5</h2>
     <table>
     <thead><tr><th>排名</th><th>错误信息</th><th>错误数量</th></tr></thead>
     <tbody>{top_error_rows}
     </tbody>
     </table>
</div>
<div class="section">
      <h2>最近10条错误日志</h2>
      <table>
      <thead><tr><th>时间</th><th>级别</th><th>错误信息</th></tr></thead>
      <tbody>{recent_errors}
      </tbody>
      </table>
</div>
<div class="footer">Powered by Log Analyzer v1.0 | 生成于 {now}</div>
</body></html>"""
