# ============ 生成模拟日志文件 ============
# 这样不依赖真实服务器日志，也能测试系统

import random
from datetime import datetime, timedelta


def generate_log(filename="sample.log", count=200):
    """生成模拟日志"""

    messages = {
        "DEBUG": [
            "用户登录请求",
            "缓存命中: user_12345",
            "执行SQL查询",
            "加载配置文件",
            "心跳检测正常",
        ],
        "INFO": [
            "服务启动成功",
            "用户注册完成",
            "订单创建成功",
            "定时任务执行完毕",
            "健康检查通过",
        ],
        "WARNING": [
            "内存使用率超过80%",
            "接口响应时间超过2秒",
            "磁盘空间不足10%",
            "连接池接近上限",
            "重试次数已达上限",
        ],
        "ERROR": [
            "数据库连接失败",
            "接口请求超时",
            "文件不存在",
            "认证失败",
            "数据格式错误",
        ],
        "CRITICAL": [
            "服务不可用",
            "数据库宕机",
            "内存溢出",
        ],
    }

    # 权重：DEBUG多， CRITICAL少
    levels = ["DEBUG"] * 40 + ["INFO"] * 30 + ["WARNING"] * 15 + ["ERROR"] * 12 + ["CRITICAL"] * 3

    start_time = datetime(2026, 9, 3, 8, 0, 0)

    with open(filename, "w", encoding="utf-8") as f:
        for i in range(count):
            level = random.choice(levels)
            msg = random.choice(messages[level])
            ts = start_time + timedelta(seconds=random.randint(0, 3600 * 12))
            f.write(f"{ts.strptime('%Y-%m-%d %H:%M:%S')} [{level}] {msg}\n")

    print(f"生成 {count} 条日志到 {filename}")


if __name__ == "__main__":
    generate_log()
