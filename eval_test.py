func_def_str = """
def test(a, b):
    return a+b
"""


def test(a, b):
    return 0


exec(func_def_str)
print(test(1, 2))

func_def_str2 = """
def test(a, b):
    return a+b+1
"""

exec(func_def_str2)
print(test(1, 2))

def test2():
    return 2

def test_exec():
    code = """
def test2():
    return 3
    """

    exec(code)
    print(test2())

test_exec()