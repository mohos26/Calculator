# 09.10.2025

import buttons
from parsing import parsing
from syntax_error import syntax_error
from buttons import clear, insert_text
from infix_to_postfix import infix_to_postfix
# from evaluate_postfix import evaluate_postfix
from threaded_evaluate import threaded_evaluate


def eq(entry):
	prompt = entry.get()
	if not prompt or prompt.startswith("Bug"):
		return
	clear(entry)
	lst = parsing(prompt)
	# debug
	print(*lst)
	if not syntax_error(lst):
		insert_text(entry, "Syntax Error")
		buttons.should_clear = True
		return
	try:
		postfix = infix_to_postfix(lst)
		threaded_evaluate(postfix, entry)
	except IndexError:
		insert_text(entry, "Syntax Error")
	except ZeroDivisionError:
		insert_text(entry, "Divide by zero")
	except ValueError:
		insert_text(entry, "Math Domain Error")
	except TimeoutError:
		insert_text(entry, "Time Out Error")
	except OverflowError:
		insert_text(entry, "+∞")
	except Exception as e:
		print(e)
		insert_text(entry, f"Bug \"{prompt}\"")
	buttons.should_clear = True
