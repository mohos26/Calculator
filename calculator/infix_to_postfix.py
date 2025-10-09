# ===============================
# infix_to_postfix.py
# Date: 26.08.2025
# Source: https://edabit.com/challenge/NZtL4MGkpCfiwShhp
# Purpose: Convert an infix expression into postfix (Reverse Polish Notation).
# Supports operators: +, -, *, /, **
# Handles precedence, associativity, and unary signs.
# ===============================


# Operator precedence dictionary
d = {
	"-":  1,
	"+":  1,
	"/":  2,
	"*":  2,
	"**": 3,
	"!":  4,
}


# Check if a token is an operator or parenthesis.
def is_operator(s):
	return s in ("/", "*", "-", "+", "**", "(", "cos(", "sin(", "tan(", "abs(", "!", ")")


def is_single_operator(s):
	return s in ("(", "cos(", "sin(", "tan(", "abs(")


# Pre-process the infix expression handel : Unary minus, Unary minus and Sign propagation
def preprocess(expr: list) -> list:
	res = []
	sing = 1
	for i, arg in enumerate(expr):
		if arg == '-':
			if not i:
				res.append("-1")
				res.append("*")
			elif expr[i - 1] in ("*", "(", "cos(", "sin(", "tan(", "abs(", "-", "+"):
				res.append("-1")
				res.append("*")
			elif expr[i - 1] in ("/", "**"):
				sing *= -1
			else:
				res.append(arg)
		elif arg == '+':
			if not i:
				continue
			elif expr[i - 1] in ("/", "*", "-", "+", "**", "(", "cos(", "sin(", "tan(", "abs("):
				continue
			else:
				res.append(arg)
		elif not is_operator(arg):
			res.append(str(float(arg) * sing))
			sing = 1
		else:
			res.append(arg)
	return res


# Convert infix expression to postfix using the Shunting Yard algorithm.
def infix_to_postfix(expr: list) -> list:
	expr = preprocess(expr)
	stack, postfix = [], []
	while expr:
		arg = expr[0]
		if is_operator(arg):
			if arg == ')':
				while not is_single_operator(stack[-1]):
					postfix.append(stack.pop())
				expr = expr[1:]
				if stack[-1] != '(':
					postfix.append(stack[-1])
				stack.pop()
			elif not stack or is_single_operator(arg) or is_single_operator(stack[-1]) or d[stack[-1]] < d[arg] or \
				(d[stack[-1]] == d[arg] and d[arg] == 3):  # this for right operators
				stack.append(arg)
				expr = expr[1:]
			else:
				postfix.append(stack.pop())
		else:
			postfix.append(arg)
			expr = expr[1:]
	while stack:
		postfix.append(stack.pop())
	return postfix
