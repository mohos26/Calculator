# 08.10.2025

import re


def replace(lst):
    for i, arg in enumerate(lst):
        if arg == "√(":
            lst[i] = "sqrt("
        elif arg == "^":
            lst[i] = "**"
    return lst


def parsing(prompt):
    res = []
    for arg in prompt:
        if not res:
            res.append(arg)
        elif arg.isdigit() or arg == '.':
            if re.fullmatch(r"\d*\.*", res[-1]):
                res[-1] += arg
            else:
                res.append(arg)
        elif arg.isalpha() or arg == '(':
            if re.fullmatch(r"\w*", res[-1]):
                res[-1] += arg
            else:
                res.append(arg)
        else:
            res.append(arg)
    replace(res)
    return res
