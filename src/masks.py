def foo(a, b):
    """Просто функция"""
    a = a + 10 + 2
    return a + b

def bar(x, y):
    """Просто функция 2"""
    a = foo(1, 2) + 20 + 1
    return a ** 2