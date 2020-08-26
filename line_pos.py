import inspect

_call_dict = {}


"""def _get_order(line, inst):
    if __file__ in _call_dict:
        if line in _call_dict[__file__]:
            _call_dict[__file__][line] += 1
            return _call_dict[__file__][line][0]
        else:
            _call_dict[__file__][line] = 1, inst
            return _call_dict[__file__][line][0]
    else:
        _call_dict[__file__] = {}
        _call_dict[__file__][line] = 1, inst
        return 1"""


def _get_order(line, inst):
    if __file__ not in _call_dict:
        _call_dict[__file__] = {}

    if line not in _call_dict[__file__]:
        _call_dict[__file__][line] = []

    try:
        index = _call_dict[__file__][line].index(inst)
    except:
        index = -1

    if index == -1:
        _call_dict[__file__][line].append(inst)
        return len(_call_dict[__file__][line])
    else:
        return index+1

def _tv():
    f = inspect.currentframe().f_back
    line = f.f_lineno
    inst = f.f_lasti

    # we need to identify each _tv() call within a file, we need them unique, otherwise, the user would have to
    # supply key name

    call_hash = line * 1000 + inst    # probably not the best idea
    call_filename = __file__

    line_order = _get_order(line, inst)

    print(f"_tv() called at {call_filename}:{line}:{line_order}")

    return 0


while True:
    a = _tv() + _tv()
