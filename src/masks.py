def foo(a, b):
    """Просто функция"""
    a = a + 10
    return a + b

def bar(x, y):
    """Просто функция 2"""
    a = foo(1, 2) + 20
    return a ** 2