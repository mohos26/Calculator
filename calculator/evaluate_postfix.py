# ===============================
# evaluate_postfix.py
# Date: 22.08.2025
# Source: https://edabit.com/challenge/xWW8PMuLN8hmAgLMJ
# Purpose: Evaluate a postfix (Reverse Polish Notation) expression.
# Supports operators: +, -, *, /, **
# ===============================


# Check if a token is a valid operator.
def is_operator(s: str) -> bool:
	return s in ("/", "*", "-", "+", "**")


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
	elif operator == '**':
		return a ** b
	raise ArithmeticError(f"Invalid Operator: {operator}")


# Evaluate a postfix expression using a stack.
def evaluate_postfix(expression: list) -> float:
	stack = []
	for arg in expression:
		if is_operator(arg):
			b, a = stack.pop(), stack.pop()  # Note: order matters (a op b)
			stack.append(apply_operator(a, arg, b))
		else:
			stack.append(float(arg))
	return stack.pop()
