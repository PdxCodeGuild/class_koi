from unit_converter import converter

def test0():
    assert converter('ft', 'm', 1) == 0.3

def test1():
    assert converter('ft', 'mi', 5280) == 1

def test2():
    assert converter('ft', 'km', 5280) == 1.6

def test3():
    assert converter('km', 'm', 3) == 3000


# def add(x, y):
#     return x + y

# def test_add_1():
#     assert add(1, 2) == 3

# def test_add_2():
#     assert add(-1, 5) == 4

# def test_add_3():
#     assert add(2, 2) == 5