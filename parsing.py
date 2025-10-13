# 08.10.2025

import re


def replace(lst):
	for i, arg in enumerate(lst):
		if arg == "√(":
			lst[i] = "sqrt("
		elif arg == "π":
			lst[i] = "3.141593"
	return lst


def parsing(prompt):
	res = []
	for arg in prompt:
		if not res:
			res.append(arg)
		elif re.fullmatch(r"\w+\d*", res[-1]) and re.fullmatch(r"[\d\w(]+", arg):
				res[-1] += arg
		elif re.fullmatch(r"[0-9.]+", res[-1]) and re.fullmatch(r"[\d.]+", arg):
				res[-1] += arg
		elif arg == "π":
			res.append("π")
		else:
			res.append(arg)
	replace(res)
	return res
