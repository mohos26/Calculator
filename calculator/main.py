"""
28.08.2025
"""

from tkinter import *
from buttons import *


if __name__ == '__main__':
    root = Tk()
    root.title("Calculator")

    window_width = 700
    window_height = 500

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.minsize(window_width, window_height)
    root.maxsize(window_width, window_height)

    for i in range(6):
        root.grid_columnconfigure(i, weight=1, minsize=70)

    for j in range(6):
        root.grid_rowconfigure(j, weight=1, minsize=70)

    entry_text = StringVar()
    entry = Entry(root, font=("Arial", 24), borderwidth=3, relief="solid", justify="right", state=DISABLED, textvariable=entry_text)
    entry.grid(row=0, column=0, columnspan=7, padx=10, pady=10, sticky="nsew", ipady=20)

    # buttons = (
    #     ('(', 1, 0), (')', 1, 1), ('rad | deg', 1, 2), ('C', 1, 3), ('ANS', 1, 4), ('/', 1, 5), ('DEL', 1, 6),
    #     ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2), ('7', 2, 3), ('8', 2, 4), ('9', 2, 5), ('*', 2, 6),
    #     ('ln', 3, 0), ('log2', 3, 1), ('log10', 3, 2), ('4', 3, 3), ('5', 3, 4), ('6', 3, 5), ('-', 3, 6),
    #     ('x^y', 4, 0), ('x^2', 4, 1), ('sqrt', 4, 2), ('1', 4, 3), ('2', 4, 4), ('3', 4, 5), ('+', 4, 6),
    #     ('abs', 5, 0), ('pi', 5, 1), ('x!', 5, 2), ('.', 5, 3), ('0', 5, 4),
    # )

    for (text, row, col, func) in buttons:
        Button(root, text=text, font=("Arial", 20), width=5, height=2, command=lambda f=func: f(entry))\
            .grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
    Button(root, text="=", font=("Arial", 24)).grid(row=5, column=5, columnspan=2, sticky="nsew")

    root.mainloop()
