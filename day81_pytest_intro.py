def test_number():
    """测试数字运算"""
    assert 2 + 3 == 5
    assert 10 - 4 == 6


def test_string():
    """测试字符串"""
    assert "hello".upper() == "HELLO"
    assert "abc" in "abcdef"


def test_list():
    """测试列表"""
    nums = [1, 2, 3]
    nums.append(4)
    assert len(nums) == 4
    assert 4 in nums


def test_dict():
    """测试字典"""
    d = {"name": "张三", "age": 20}
    assert d["name"] == "张三"
    d["age"] = 21
    assert d.get("age") == 21
