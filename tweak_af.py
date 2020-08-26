# inspired by: https://github.com/joeld42/ld48jovoc/blob/master/util/tweakval/tweakval.cpp

import inspect

tweak_dict = {}
_call_dict = {}

token_name = "_t" + "v" + "("
token_length = len(token_name)


def reload_dict(call_filename):
    with open(call_filename, "r") as f:
        content = f.readlines()

    content = [x.strip() for x in content]  # strip whitespaces

    line_counter = 0

    for line in content:
        start = 0

        found_on_line_counter = 0

        while True:
            index = line.find(token_name, start)

            if index == -1:
                break

            if line.find("def") != -1 or line.startswith("#"):
                break

            start = index + 1

            value_index = index + token_length
            value_end = line.find(")", value_index)

            value = line[value_index: value_end]

            if len(value) == 0:
                break

            found_on_line_counter += 1

            if call_filename not in tweak_dict:
                tweak_dict[call_filename] = {}

            if (line_counter + 1) not in tweak_dict[call_filename]:
                tweak_dict[call_filename][(line_counter + 1)] = {}

            tweak_dict[call_filename][(line_counter + 1)][found_on_line_counter] = int(value)

        line_counter += 1


def resolve_value(default_value, call_filename, line, line_order):
    reload_dict(call_filename)

    if call_filename in tweak_dict and line in tweak_dict[call_filename] \
            and line_order in tweak_dict[call_filename][line]:
        return tweak_dict[call_filename][line][line_order]
    else:
        return default_value


def _get_order(line, inst):
    if __file__ not in _call_dict:
        _call_dict[__file__] = {}

    if line not in _call_dict[__file__]:
        _call_dict[__file__][line] = []

    try:
        index = _call_dict[__file__][line].index(inst)
    except ValueError:
        index = -1

    if index == -1:
        _call_dict[__file__][line].append(inst)
        return len(_call_dict[__file__][line])
    else:
        return index + 1


def _tv(default_value):
    f = inspect.currentframe().f_back
    line = f.f_lineno
    inst = f.f_lasti

    # we need to identify each _tv() call within a file, we need them unique, otherwise, the user would have to
    # supply key name

    call_filename = __file__

    line_order = _get_order(line, inst)

    # print(f"_tv() called at {call_filename}:{line}:{line_order}")

    return resolve_value(default_value, call_filename, line, line_order)


def test_func_inner():
    print(f"inner: {_tv(8)}")


def test_func():
    a = _tv(00)
    b = _tv(10)
    c = _tv(2) + _tv(3)

    print(f"{a}, {b}")

    while True:
        print(_tv(2), _tv(4))
        test_func_inner()


if __name__ == '__main__':
    test_func()
