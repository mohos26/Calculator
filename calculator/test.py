from infix_to_postfix import infix_to_postfix
from evaluate_postfix import evaluate_postfix
from math import *


file = open("test.txt")

for i, expr in enumerate(file.read().split('\n')):
    i += 1
    if '=' in expr:
        expr, answer = expr.split('=')
        postfix_var = infix_to_postfix(expr.split())
        answer = int(answer)
    else:
        postfix_var = infix_to_postfix(expr.split())
        answer = round(eval(expr), 6)
    result = round(evaluate_postfix(postfix_var), 6)
    #try:
    #    result = round(evaluate_postfix(postfix_var), 6)
    #except:
    #    print("Error compilation")
    #    result = float("inf")
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
