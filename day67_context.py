class PowerSwitch:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"开灯：{self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"关灯: {self.name}")
        print(f"异常情况 {exc_type} / {exc_val}")
        return False


with PowerSwitch("客厅灯") as light:
    print(f"{light.name} 亮着，干点活...")
    1 / 0
