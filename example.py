# 1. just start the script and let it running
# 2. edit this source file in IDE or in another terminal

from tweak_af import tv, tf


# 3. try to change body of this function - while the original script is still running
def test_func(a, b):
    return str(a + b) + " " + "test"

def str_test_func(param):
    return "badass " + param


if __name__ == '__main__':
    while True:
        # 4. try to change the tweakable value (3) to something else - while the original script is still running
        print(tf(lambda: test_func(1, tv(3))))
        print(tf(lambda: str_test_func(tv("tomas"))))

# 5. you can break tv() logic by adding new lines above it, but tf() will work when adding new lines to functions
