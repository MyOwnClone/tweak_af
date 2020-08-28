from tweak_af import tv, tf


def test_func(a, b):
    return str(a + b) + " " + "test"

def str_test_func(param):
    return "badass " + param


if __name__ == '__main__':
    while True:
        print(tf(lambda: test_func(1, tv(3))))
        print(tf(lambda: str_test_func(tv("tomas"))))
