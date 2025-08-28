# 26.08.2025


d = {
	"/":  2,
	"*":  2,
	"-":  1,
	"+":  1,
	"**": 3,
}


def is_operator(s):
	return s in ("/", "*", "-", "+", "**", "(", ")")


def infix_to_postfix(expr: list) -> list:
	stack, postfix = [], []
	while expr:
		arg = expr[0]
		if is_operator(arg):
			if arg == ')':
				while stack[-1] != '(':
					postfix.append(stack.pop())
				expr = expr[1:]
				stack.pop()
			elif not stack or '(' in (arg, stack[-1]) or d[stack[-1]] < d[arg]:
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
