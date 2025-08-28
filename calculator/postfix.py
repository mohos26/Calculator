# 22.08.2025


def is_operator(s: str) -> bool:
	return s in ("/", "*", "-", "+", "**")


def ft_aid(a: float, operator: str, b: float) -> float:
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


def postfix(expression: list) -> float:
	stack = []
	for arg in expression:
		if is_operator(arg):
			b, a = stack.pop(), stack.pop()
			stack.append(ft_aid(a, arg, b))
		else:
			stack.append(float(arg))
	return stack.pop()
