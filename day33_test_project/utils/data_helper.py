# 测试数据管理
import csv
import json
from pathlib import Path
from day33_test_project.config import Config


def load_csv(filename):
    """从CSV加载测试数据"""
    filepath = Path(Config.DATA_DIR) / filename
    data = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data


def load_json(filename):
    """从JSON加载测试数据"""
    filepath = Path(Config.DATA_DIR) / filename
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)