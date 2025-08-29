from infix_to_postfix import infix_to_postfix
from postfix import postfix


file = open("test.txt")

for i, expr in enumerate(file.read().split('\n')):
    i += 1
    postfix_var = infix_to_postfix(expr.split())
    answer = round(eval(expr), 6)
    result = round(postfix(postfix_var), 6)
    if result != answer:
        print(f"Test {i} !!! Fail !!!")
        print(f"expression: {expr}")
        print(f"postfix: ", *postfix_var)
        print(f"output: {result}")
        print(f"answer: {answer}")
        break
    else:
        print(f"Test {i} pass")
else:
    print("!!! All Test Pass !!!")
