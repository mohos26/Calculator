# 07.10.2025

from tkinter import *
# import pyperclip


should_clear = False


def insert_text(entry, text):
	global should_clear
	if should_clear:
		clear(entry)
	should_clear = False
	entry.config(state=NORMAL)
	entry.insert(END, text)
	entry.config(state=DISABLED)


def zero(entry):
	insert_text(entry, "0")


def one(entry):
	insert_text(entry, "1")


def two(entry):
	insert_text(entry, "2")


def three(entry):
	insert_text(entry, "3")


def four(entry):
	insert_text(entry, "4")


def five(entry):
	insert_text(entry, "5")


def six(entry):
	insert_text(entry, "6")


def seven(entry):
	insert_text(entry, "7")


def eight(entry):
	insert_text(entry, "8")


def nine(entry):
	insert_text(entry, "9")


def open_bracket(entry):
	insert_text(entry, "(")


def close_bracket(entry):
	insert_text(entry, ")")


def clear(entry):
	entry.config(state=NORMAL)
	entry.delete(0, END)
	entry.config(state=DISABLED)


def mod(entry):
	insert_text(entry, "%")


def div(entry):
	insert_text(entry, "/")


def mul(entry):
	insert_text(entry, "*")


def add(entry):
	insert_text(entry, "+")


def sub(entry):
	insert_text(entry, "-")


def sin(entry):
	insert_text(entry, "sin(")


def cos(entry):
	insert_text(entry, "cos(")


def tan(entry):
	insert_text(entry, "tan(")


def ln(entry):
	insert_text(entry, "ln(")


def log2(entry):
	insert_text(entry, "log2(")


def log10(entry):
	insert_text(entry, "log10(")


def power(entry):
	insert_text(entry, "^")


def power2(entry):
	insert_text(entry, "^2")


def sqrt(entry):
	insert_text(entry, "√(")


def abs(entry):
	insert_text(entry, "abs(")


def pi(entry):
	insert_text(entry, "π")


def factorial(entry):
	insert_text(entry, "fac(")


def dot(entry):
	insert_text(entry, ".")


def e(entry):
	insert_text(entry, "e")


def delete(entry):
	global should_clear
	if should_clear:
		clear(entry)
		should_clear = False
		return
	length = len(entry.get())
	if not length:
		return
	entry.config(state=NORMAL)
	entry.delete(length - 1, length)
	entry.config(state=DISABLED)


buttons = (
	('(', 1, 0, open_bracket, "Spec.TButton"),
	(')', 1, 1, close_bracket, "Spec.TButton"),
	('e', 1, 2, e, "Spec.TButton"),
	('C', 1, 3, clear, "Spec.TButton"),
	('mod', 1, 4, mod, "Spec.TButton"),
	('/', 1, 5, div, "Spec.TButton"),
	('DEL', 1, 6, delete, "Spec.TButton"),
	('sin', 2, 0, sin, "Spec.TButton"),
	('cos', 2, 1, cos, "Spec.TButton"),
	('tan', 2, 2, tan, "Spec.TButton"),
	('7', 2, 3, seven, "Num.TButton"),
	('8', 2, 4, eight, "Num.TButton"),
	('9', 2, 5, nine, "Num.TButton"),
	('*', 2, 6, mul, "Spec.TButton"),
	('ln', 3, 0, ln, "Spec.TButton"),
	('log2', 3, 1, log2, "Spec.TButton"),
	('log10', 3, 2, log10, "Spec.TButton"),
	('4', 3, 3, four, "Num.TButton"),
	('5', 3, 4, five, "Num.TButton"),
	('6', 3, 5, six, "Num.TButton"),
	('-', 3, 6, sub, "Spec.TButton"),
	('x^y', 4, 0, power, "Spec.TButton"),
	('x^2', 4, 1, power2, "Spec.TButton"),
	('√', 4, 2, sqrt, "Spec.TButton"),
	('1', 4, 3, one, "Num.TButton"),
	('2', 4, 4, two, "Num.TButton"),
	('3', 4, 5, three, "Num.TButton"),
	('+', 4, 6, add, "Spec.TButton"),
	('abs', 5, 0, abs, "Spec.TButton"),
	('π', 5, 1, pi, "Spec.TButton"),
	('x!', 5, 2, factorial, "Spec.TButton"),
	('.', 5, 3, dot, "Num.TButton"),
	('0', 5, 4, zero, "Num.TButton"),
)
