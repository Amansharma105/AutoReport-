def test_add():
    assert 2 + 2 == 4

def test_subtract():
    assert 5 - 2 == 3

def test_multiply():
    assert 3 * 4 == 12

def test_divide():
    assert 8 / 2 == 4

def test_string():
    assert "Auto" + "Report" == "AutoReport"

def test_list():
    assert len([1, 2, 3]) == 3

def test_boolean():
    assert True

def test_max():
    assert max(1, 5, 3) == 5

def test_min():
    assert min(1, 5, 3) == 1

def test_sum():
    assert sum([1, 2, 3]) == 6

def test_type():
    assert isinstance(5, int)

def test_upper():
    assert "hello".upper() == "HELLO"

def test_lower():
    assert "HELLO".lower() == "hello"

def test_contains():
    assert "Report" in "AutoReport"

def test_length():
    assert len("Python") == 6
