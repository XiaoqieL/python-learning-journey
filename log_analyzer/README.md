# 智能日志分析系统

一个用 Python 开发的日志分析工具，支持日志解析、统计分析、HTML可视化报告。

## 功能

- 解析标准格式日志文件
- 按级别统计（DEBUG/INFO/WARNING/ERROR/CRITICAL）
- 错误消息频率TOP5统计
- 按级别过滤日志
- 关键词搜索
- 生成可视化HTML报告（柱状图+表格）
- 模拟日志生成器（测试用）

## 技术栈

- Python 3.12
- re（正则解析）
- collections.Counter（频率统计）
- dataclasses（数据模型）

## 项目结构
