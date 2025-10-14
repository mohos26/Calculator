# ===============================
# evaluate_postfix.py
# Date: 22.08.2025
# Source: https://edabit.com/challenge/xWW8PMuLN8hmAgLMJ
# Purpose: Evaluate a postfix (Reverse Polish Notation) expression.
# ===============================

from math import *


# Check if a token is a valid operator.
def is_operator(s: str) -> bool:
	return s in ("/", "*", "-", "+", "^", "%")


def is_single_operator(s):
	return s in ("(", "sin(", "cos(", "tan(", "ln(", "log2(", "log10(", "sqrt(", "abs(", "fac(")


# Perform arithmetic operation
def apply_operator(a: float, operator: str, b: float) -> float:
	if operator == '+':
		return a + b
	elif operator == '-':
		return a - b
	elif operator == '/':
		return a / b
	elif operator == '*':
		return a * b
	elif operator == '^':
		return a ** b
	elif operator == '%':
		return a % b
	raise ArithmeticError(f"Invalid Operator: {operator}")


def apply_single_operator(a: float, operator: str) -> float:
	if operator == "cos(":
		return cos(a)
	elif operator == "sin(":
		return sin(a)
	elif operator == "tan(":
		return tan(a)
	elif operator == "abs(":
		return abs(a)
	elif operator == "fac(":
		return gamma(a + 1)
	elif operator == "ln(":
		return log(a)
	elif operator == "log10(":
		return log10(a)
	elif operator == "log2(":
		return log2(a)
	elif operator == "sqrt(":
		return sqrt(a)
	raise ArithmeticError(f"Invalid Operator: {operator}")


# Evaluate a postfix expression using a stack.
def evaluate_postfix(expression: list) -> float:
	stack = []
	for arg in expression:
		if is_operator(arg):
			b, a = stack.pop(), stack.pop()  # Note: order matters (a op b)
			stack.append(apply_operator(a, arg, b))
		elif is_single_operator(arg):
			a = stack.pop()
			stack.append(apply_single_operator(a, arg))
		else:
			stack.append(float(arg))
	res = stack.pop()
	if stack:
		raise IndexError
	return res
