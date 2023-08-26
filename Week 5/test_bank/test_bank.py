from bank import value

def test_0():
    assert value("hello") == 0

def test_20():
    assert value("hey") == 20

def test_100():
    assert value("oh") == 100

def test_case_sensitivity():
    assert value("Hello") == 0