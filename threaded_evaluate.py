import threading
from buttons import insert_text
from evaluate_postfix import evaluate_postfix

res = None
errno = None

def to_int_if_possible(n):
	if n == int(n):
		return int(n)
	return n


def background_eval(postfix):
	global res, errno
	try:
		res = evaluate_postfix(postfix)
	except Exception as e:
		errno = e


def threaded_evaluate(postfix, entry):
	global res, errno
	thread = threading.Thread(target=background_eval, args=(postfix,))
	thread.start()
	thread.join(timeout=1)
	if errno:
		tmp = errno
		errno = None
		raise tmp
	if res == None:
		raise TimeoutError
	if res > 1_000_000_000_000:
		insert_text(entry, "+∞")
	elif res < -1_000_000_000_000:
		insert_text(entry, "-∞")
	else:
		insert_text(entry, to_int_if_possible(res))
	res = None
