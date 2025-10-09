# 09.10.2025

from parsing import parsing
from buttons import clear, insert_text
from syntax_error import syntax_error
from infix_to_postfix import infix_to_postfix
from evaluate_postfix import evaluate_postfix


def ft_aid(n):
    if n == int(n):
        return int(n)
    return n


def eq(entry):
    prompt = entry.get()
    if not prompt or prompt.startswith("Bug"):
        return
    clear(entry)
    lst = parsing(prompt)
    if not syntax_error(lst):
        insert_text(entry, "Syntax Error")
        return
    try:
        postfix = infix_to_postfix(lst)
        insert_text(entry, ft_aid(evaluate_postfix(postfix)))
    except IndexError:
        insert_text(entry, "Syntax Error")
    except Exception as e:
        print(e)
        insert_text(entry, f"Bug \"{prompt}\"")
