# 09.10.2025

import buttons
from parsing import parsing
from syntax_error import syntax_error
from buttons import clear, insert_text
from infix_to_postfix import infix_to_postfix
# from evaluate_postfix import evaluate_postfix
from aid_file import ft_aid


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
		# res = evaluate_postfix(postfix)
		# if res > 1_000_000_000_000:
		# 	insert_text(entry, "+∞")
		# elif res < -1_000_000_000_000:
		# 	insert_text(entry, "-∞")
		# else:
		# 	insert_text(entry, to_int_if_possible(res))
		ft_aid(postfix, entry)
	except IndexError:
		insert_text(entry, "Syntax Error")
	except ZeroDivisionError:
		insert_text(entry, "Divide by zero")
	except ValueError:
		insert_text(entry, "Math Domain Error")
	except TimeoutError:
		insert_text(entry, "Time Out Error")
	except Exception as e:
		print(e)
		insert_text(entry, f"Bug \"{prompt}\"")
	buttons.should_clear = True
