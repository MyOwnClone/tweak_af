from tweak_af import tv, reload_functions, tweakable


def inner_test_func():
    return "inner_badassis"

# @tweakable
def test_func():
    return "dummy" + "1" + inner_test_func() + "3"


if __name__ == '__main__':
    # val = tv(0)

    while True:
        # print(tv(3.14))
        reload_functions()
        print(test_func())
