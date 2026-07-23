# 文件操作工具
import json
from pathlib import Path


def save_students(students, filename):
    """保存学生列表到JSON文件"""
    data = [s.to_dict() for s in students]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"已保存{len(students)} 条记录到 {filename}")


def load_students(filename):
    """从JSON文件读取学生数据"""
    path = Path(filename)
    if not path.exists():
        print(f"文件 {filename} 不存在")
        return []

    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"从{filename} 读取了 {len(data)} 条记录")
    return data
