# 07.10.2025

from tkinter import *


def zero(entry):
    entry.insert(END, "0")


def one(entry):
    entry.config(state=NORMAL)
    entry.insert(END, "1")
    entry.config(state=DISABLED)


def two(entry):
    entry.insert(END, "2")


def three(entry):
    entry.insert(END, "3")


def four(entry):
    entry.insert(END, "4")


def five(entry):
    entry.insert(END, "5")


def six(entry):
    entry.insert(END, "6")


def seven(entry):
    entry.insert(END, "7")


def eight(entry):
    entry.insert(END, "8")


def nine(entry):
    entry.insert(END, "9")


def open_bracket(entry):
    entry.insert(END, "(")


def close_bracket(entry):
    entry.insert(END, ")")


def clear(entry):
    entry.delete(0, END)


def ans(entry):
    pass


def div(entry):
    entry.insert(END, "/")


def mul(entry):
    entry.insert(END, "*")


def add(entry):
    entry.insert(END, "+")


def sub(entry):
    entry.insert(END, "-")


def sin(entry):
    entry.insert(END, "sin(")


def cos(entry):
    entry.insert(END, "cos(")


def tan(entry):
    entry.insert(END, "tan(")


def ln(entry):
    entry.insert(END, "ln(")


def log2(entry):
    entry.insert(END, "log2(")


def log10(entry):
    entry.insert(END, "log10(")


def power(entry):
    entry.insert(END, "^")


def power2(entry):
    entry.insert(END, "^2")


def sqrt(entry):
    entry.insert(END, "√(")


def abs(entry):
    entry.insert(END, "√(")


def pi(entry):
    pass


def factorial(entry):
    entry.insert(END, "!")


def dot(entry):
    entry.insert(END, ".")


def eq(entry):
    pass


def angle_unit(entry):
    pass


def delete(entry):
    pass


buttons = (
    ('(', 1, 0, open_bracket), (')', 1, 1, close_bracket), ('rad | deg', 1, 2, angle_unit), ('C', 1, 3, clear), ('ANS', 1, 4, ans), ('/', 1, 5, div), ('DEL', 1, 6, delete),
    ('sin', 2, 0, sin), ('cos', 2, 1, cos), ('tan', 2, 2, tan), ('7', 2, 3, seven), ('8', 2, 4, eight), ('9', 2, 5, nine), ('*', 2, 6, mul),
    ('ln', 3, 0, ln), ('log2', 3, 1, log2), ('log10', 3, 2, log10), ('4', 3, 3, four), ('5', 3, 4, five), ('6', 3, 5, six), ('-', 3, 6, sub),
    ('x^y', 4, 0, power), ('x^2', 4, 1, power2), ('sqrt', 4, 2, sqrt), ('1', 4, 3, one), ('2', 4, 4, two), ('3', 4, 5, three), ('+', 4, 6, add),
    ('abs', 5, 0, abs), ('pi', 5, 1, pi), ('x!', 5, 2, factorial), ('.', 5, 3, dot), ('0', 5, 4, zero),
)
