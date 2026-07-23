# 字符串工具
import re


def extract_number(text):
    """从文本中提取所有数字"""
    return [int(n) for n in re.findall(r"\d+", text)]


def mask_phone(text):
    """手机号脱敏：138****5678"""
    return re.sub(r"(\d{3})\d{4}(\d{4})", r"\1****\2", text)


def clean_text(text):
    """清理文本：去首尾空格、去多余空格"""
    return " ".join(text.strip().split())
