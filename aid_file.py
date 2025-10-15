import threading
from time import sleep
from buttons import insert_text
from evaluate_postfix import evaluate_postfix

res = None


def to_int_if_possible(n):
	if n == int(n):
		return int(n)
	return n


def ft_aid2(postfix):
	global res
	res = evaluate_postfix(postfix)


def ft_aid(postfix, entry):
	global res
	thread = threading.Thread(target=ft_aid2, args=(postfix,))
	thread.start()
	thread.join(timeout=0.1)
	if res == None:
		raise TimeoutError
	if res > 1_000_000_000_000:
		insert_text(entry, "+∞")
	elif res < -1_000_000_000_000:
		insert_text(entry, "-∞")
	else:
		insert_text(entry, to_int_if_possible(res))
	res = None
