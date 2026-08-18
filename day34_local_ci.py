# ============ 第三十四天：本地CI模拟器 ============
# 模拟 GitHub Actions 的完整流程：拉代码 → 装依赖 → 跑测试 → 出报告

import subprocess
import sys
import time
import os
import shutil
from pathlib import Path
from datetime import datetime


class LocalCI:
    """本地持续集成模拟器"""

    def __init__(self, project_dir, test_dir="test"):
        self.project_dir = Path(project_dir)
        self.test_dir = self.project_dir / test_dir
        self.report_dir = self.project_dir / "ci_reports"
        self.passed = 0
        self.failed = 0
        self.errors = 0
        self.start_time = None

    def _log(self, step, msg, status="INFO"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        symbols = {"INFO": "→", "PASS": "✓", "FAIL": "✗", "WARN": "!"}
        symbols = symbols.get(status, "→")
        print(f"[{timestamp}] [{step:>12}] {symbols} {msg}")

    def run(self):
        """执行完整CI流程"""
        print("=" * 60)
        print("   本地CI模拟器 - Local Continuous Integration")
        print("=" * 60)
        print()

        self.start_time = time.time()

        # Step 1: 环境检查
        self._step_environment()

        # Step 2: 安装依赖
        self._step_install()

        # Step 3: 运行测试
        self._step_test()

        # Step 4: 生成报告
        self._step_report()

        # Step 5:清理
        self._summary()

    def _step_environment(self):
        """Step 1: 环境检查"""
        self._log("environment", "检查运行环境...")

        # Python版本
        version = sys.version.split()[0]
        self._log("environment", f"Python {version}")

        # 项目目录
        if not self.project_dir.exists():
            self._log("environment", f"项目目录不存在：{self.project_dir}", "FAIL")
            sys.exit(1)

        # 测试目录
        test_files = list(self.test_dir.glob("test_*.py")) if self.test_dir.exists() else []
        if not test_files:
            self._log("environment", f"未找到测试文件,使用day33项目", "WARN")
        else:
            self._log("environment", f"找到测试文件：{len(test_files)} 个测试文件", "PASS")

    def _step_install(self):
        """Step 2: 安装依赖"""
        self._log("install", "检查依赖...")
        deps = ["pytest", "requests", "playwright"]
        for dep in deps:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "show", dep],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                version_line = [l for l in result.stdout.split('\n') if 'Version' in l]
                ver = version_line[0].split(': ')[1] if version_line else "?"
                self._log("install", f"{dep} {ver} 已安装", "PASS")
            else:
                self._log("install", f"{dep} 未安装，正在安装...", "WARN")
                subprocess.run([sys.executable, "-m", "pip", "install", dep], capture_output=True)

    def _step_test(self):
        """Step 3: 运行测试"""
        self._log("test", "开始执行测试套件...")
        print()

        # 创建报告目录
        self.report_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = self.report_dir / f"report_{timestamp}.html"

        # 运行 pytest
        cmd = [
            sys.executable,
            "-m",
            "pytest",
            str(self.test_dir) if self.test_dir.exists() else "day33_test_project/test",
            "-v",
            "--tb=short",
            f"--html={report_file}",
            "--self-contained-html"

        ]

        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(self.project_dir))

        # 解析结果
        output = result.stdout
        print(output)

        # 统计
        for line in output.split("\n"):
            if "passed" in line and "failed" in line:
                self._log("test", line.strip(), "PASS" if 'failed' not in line or '0 failed' in line else "FAIL")
            elif line.strip().endswith('passed') and 'failed' not in line:
                self._log("test", line.strip(), "PASS")

        if result.returncode == 0:
            self._log("test", f"测试报告: {report_file}", "PASS")
        else:
            self._log("test", f"有测试失败，报告：{report_file}", "FAIL")

    def _step_report(self):
        """Step 4: 生成CI摘要"""
        self._log("report", "生成CI摘要...")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        summary_file = self.report_dir / f"summary_{timestamp}.json"

        import json
        elapsed = time.time() - self.start_time

        summary = {
            "ci_run_id": timestamp,
            "timestamp": datetime.now().isoformat(),
            "duration_seconds": round(elapsed, 2),
            "status": "PASS" if self.failed == 0 else "FAIL",
            "project": str(self.project_dir.name),
        }

        with open(summary_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        self._log("report", f"摘要已保存：{summary_file}", "PASS")

    def _summary(self):
        """Step 5: 最终摘要"""
        elapsed = time.time() - self.start_time
        print()
        print("=" * 60)
        print("   CI 流程完成！")
        print("=" * 60)
        print(f"总耗时：{elapsed:.1f} 秒")
        print(f"   报告目录：{self.report_dir.absolute()}")
        print()
        print("  CI流程说明:")
        print("    1. 检查环境 (Python版本、依赖)")
        print("    2. 安装缺失依赖")
        print("    3. 自动运行全部测试")
        print("    4. 生成HTML报告 + JSON摘要")
        print("    5. 测试失败则CI失败（阻止代码合并）")
        print("=" * 60)


if __name__ == "__main__":
    # 运行CI（指向day33的测试项目）
    project = sys.argv[1] if len(sys.argv) > 1 else "day33_test_project"
    ci = LocalCI(project)
    ci.run()
