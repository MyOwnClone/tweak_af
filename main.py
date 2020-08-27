from tweak_af import tv, reload_func_dict, tweakable


def inner_test_func():
    return "inner_badass"

#@tweakable
def test_func():
    return "dummy" + "1" + inner_test_func()


if __name__ == '__main__':
    # val = tv(0)

    while True:
        # print(tv(0))
        reload_func_dict()
        print(test_func())
