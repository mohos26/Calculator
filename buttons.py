# 07.10.2025

from tkinter import *


def insert_text(entry, text):
	if entry.get().startswith("Syntax") or entry.get().startswith("Bug"):
		clear(entry)
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


def ans(entry):
	pass


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


def angle_unit(entry):
	pass


def delete(entry):
	length = len(entry.get())
	if not length:
		return
	entry.config(state=NORMAL)
	entry.delete(length - 1, length)
	entry.config(state=DISABLED)

buttons = (
	('(', 1, 0, open_bracket), (')', 1, 1, close_bracket), ('rad | deg', 1, 2, angle_unit), ('C', 1, 3, clear),
	('ANS', 1, 4, ans), ('/', 1, 5, div), ('DEL', 1, 6, delete), ('sin', 2, 0, sin), ('cos', 2, 1, cos),
	('tan', 2, 2, tan), ('7', 2, 3, seven), ('8', 2, 4, eight), ('9', 2, 5, nine), ('*', 2, 6, mul), ('ln', 3, 0, ln),
	('log2', 3, 1, log2), ('log10', 3, 2, log10), ('4', 3, 3, four), ('5', 3, 4, five), ('6', 3, 5, six),
	('-', 3, 6, sub), ('x^y', 4, 0, power), ('x^2', 4, 1, power2), ('sqrt', 4, 2, sqrt), ('1', 4, 3, one),
	('2', 4, 4, two), ('3', 4, 5, three), ('+', 4, 6, add), ('abs', 5, 0, abs), ('pi', 5, 1, pi),
	('x!', 5, 2, factorial), ('.', 5, 3, dot), ('0', 5, 4, zero),
)
