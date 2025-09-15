def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_list_math():
    xs = [1, 2, 3]
    assert len(xs) == 3
    assert sum(xs) == 6
