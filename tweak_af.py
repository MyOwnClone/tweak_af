# tool for live coding and tweaking long running scripts (ML training, crawlers)
# inspired by: https://github.com/joeld42/ld48jovoc/blob/master/util/tweakval/tweakval.cpp

import inspect

_tweak_dict = {}
_call_dict = {}

_token_name = "t" + "v" + "("   # to not confuse our "parser"
_token_length = len(_token_name)

_g_tv_enabled = True


def set_tweakables_enabled(enabled):
    global _g_tv_enabled
    _g_tv_enabled = enabled

# TODO: use fs_notify and reload only when backing file changes
def _reload_tv_dict(call_filename):
    with open(call_filename, "r") as f:
        content = f.readlines()

    content = [x.strip() for x in content]  # strip whitespaces

    line_counter = 0

    for line in content:
        start = 0

        found_on_line_counter = 0

        while True:
            index = line.find(_token_name, start)

            if index == -1:
                break

            if line.find("def") != -1 or line.startswith("#"):
                break

            start = index + 1

            value_index = index + _token_length
            value_end = line.find(")", value_index)

            value = line[value_index: value_end]

            if len(value) == 0:
                break

            found_on_line_counter += 1

            if call_filename not in _tweak_dict:
                _tweak_dict[call_filename] = {}  # TODO: rewrite

            if (line_counter + 1) not in _tweak_dict[call_filename]:
                _tweak_dict[call_filename][(line_counter + 1)] = {}  # TODO: rewrite

            _tweak_dict[call_filename][(line_counter + 1)][found_on_line_counter] = eval(value)

        line_counter += 1


# TODO: use fs_notify and reload only when backing file changes
def _reload_functions(globals_param=None, call_filename=None):
    if globals_param is None:
        f = inspect.currentframe().f_back
        globals_param = f.f_globals

    if call_filename is None:
        call_filename = inspect.stack()[1][1]

    with open(call_filename, "r") as f:
        content = f.readlines()

    inside_function = False
    function_indentation = -1
    function_line_start = -1

    def_token = "def"
    def_token_length = len(def_token)

    line_index = 0

    # TODO: rewrite the continue parts

    for line in content:

        if len(line.strip()) == 0:
            line_index += 1  # :-(
            continue

        if inside_function:
            index = 0

            while index < len(line) and line[index].isspace():
                index += 1

            indentation = index

            if indentation <= function_indentation:  # end of previous func definition
                func_lines = content[function_line_start-1:line_index]

                # print(func_lines)

                code = ''.join(cur_line for cur_line in func_lines)

                exec(code, globals_param)

                inside_function = False

        index = line.find(def_token)
        line_length = len(line)
        if index != -1:
            if index > 0 and line[index-1] == "\"":
                line_index += 1  # :-(
                continue

            index_backup = index

            index += def_token_length
            start_index = index

            while index < line_length and line[index].isspace():
                index += 1

            name_start = -1
            name_end = -1

            # skip variable definitions named with "def_"
            if index == start_index:
                line_index += 1  # :-(
                continue

            inside_function = True
            function_indentation = index_backup

            if index < line_length:
                name_start = index

                while index < line_length and (line[index].isalnum() or line[index] == '_'):
                    index += 1

                name_end = index

            if name_start != -1 and name_end != -1:
                function_line_start = line_index

                line_index += 1  # :-(

                continue

        line_index += 1

# terrible usage of dict(), I know, TODO: rewrite
def _resolve_value(default_value, call_filename, line, line_order):
    _reload_tv_dict(call_filename)

    if call_filename in _tweak_dict and line in _tweak_dict[call_filename] \
            and line_order in _tweak_dict[call_filename][line]:  # TODO: rewrite
        return _tweak_dict[call_filename][line][line_order]  # TODO: rewrite
    else:
        return default_value


# terrible usage of dict(), I know, TODO: rewrite
def _get_call_order(line, inst):
    if __file__ not in _call_dict:
        _call_dict[__file__] = {}   # TODO: rewrite

    if line not in _call_dict[__file__]:
        _call_dict[__file__][line] = []

    try:
        index = _call_dict[__file__][line].index(inst)  # TODO: rewrite
    except ValueError:
        index = -1

    if index == -1:
        _call_dict[__file__][line].append(inst) # TODO: rewrite
        return len(_call_dict[__file__][line])  # TODO: rewrite
    else:
        return index + 1


# tv stands for "tweakable value"
def tv(default_value):
    if not _g_tv_enabled:
        return default_value

    f = inspect.currentframe().f_back
    line = f.f_lineno
    bytecode_instruction_offset = f.f_lasti

    # we need to identify each _tv() call within a file, we need them unique, otherwise, the user would have to
    # supply key name

    call_filename = inspect.stack()[1][1]

    line_call_order = _get_call_order(line, bytecode_instruction_offset)

    # print(f"_tv() called at {call_filename}:{line}:{line_call_order}")

    return _resolve_value(default_value, call_filename, line, line_call_order)


# "tweakable function"
def tf(f):
    if not _g_tv_enabled:
        return f()

    frame = inspect.currentframe().f_back
    _reload_functions(frame.f_globals, inspect.stack()[1][1])

    return f()
