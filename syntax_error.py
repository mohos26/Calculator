# 09.102025

import re


def bracket_checker(lst):
	instruction = {"(", "sin(", "cos(", "tan(", "ln(", "log2(", "log10(", "sqrt(", "abs(", "fac("}
	res = 0
	for arg in lst:
		if arg in instruction:
			res += 1
		elif arg == ')':
			res -= 1
	return not res


def syntax_error(lst):
	instruction = {"(", ")", "/", "sin(", "cos(", "tan(", "*", "ln(",
				"log2(", "log10(", "-", "^", "sqrt(", "+", "abs(", "fac("}
	for arg in lst:
		if arg not in instruction and not re.fullmatch(r"\d+\.?\d*", arg):
			return False
	return bracket_checker(lst)
