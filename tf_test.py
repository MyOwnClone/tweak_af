from tweak_af import tf

def dummy_function():
    print("I do almost nothing!")
    return 0


while True:
    returned_value = tf(lambda: dummy_function())

    if returned_value == 42:
        exit(0)
