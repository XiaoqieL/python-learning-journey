import logging

logging.basicConfig(
    level=logging.DEBUG,  # 日志级别：DEBUG < INFO < WARNING < ERROR < CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",  # 写进文件，不写就只打印到屏幕
    filemode="a",  # a=追加（默认），w=覆盖
)

logging.debug("调试信息")  # 最低级，开发用
logging.info("普通信息")  # 日常记录
logging.warning("警告")  # 不对劲但还能跑
logging.error("错误")  # 出问题了


def divide(a, b):
    logging.info(f"计算{a} / {b}")
    try:
        result = a / b
        logging.info(f"结果：{result}")
        return result
    except ZeroDivisionError:
        logging.error("除数不能为零")
        return None


divide(0, 10)
divide(10, 0)
divide(8, 4)
