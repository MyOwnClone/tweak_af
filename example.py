# 1. just start the script and let it running
# 2. edit this source file in IDE or in another terminal

from tweak_af import tv, tf  # , set_tweakables_enabled


def func_called_from_tweakable():
    return 42  # if you uncomment the call in test_func() during the runtime, try to change this function too


# 3. try to change body of this function - while the original script is still running
# Try to uncomment the part in the return statement (during the runtime), save it and see the change
def test_func(a, b):
    return a + b  # + func_called_from_tweakable()


def str_test_func(param):
    return "badass " + param


if __name__ == '__main__':
    # set_tweakables_enabled(False)  # use this to disable tv/tf functions, in this case, they will return defaults or act as pass through

    while True:
        # 4. try to change the tweakable value (3) to something else - while the original script is still running
        print(tf(lambda: test_func(1, tv(3))))  # lambda is currently needed, because reasons :-)
        print(tf(lambda: str_test_func(tv("original"))))

# Optional: 5. you can break tv() logic by adding new lines above it, but tf() will work when adding new lines to functions
