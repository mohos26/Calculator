"""
28.08.2025
"""

from tkinter import *
from buttons import buttons
from eq import eq


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

	entry = Entry(root, font=("Arial", 24), borderwidth=3, relief="solid", justify="right", state=DISABLED)
	entry.grid(row=0, column=0, columnspan=7, padx=10, pady=10, sticky="nsew", ipady=20)

	for (text, row, col, func) in buttons:
		Button(root, text=text, font=("Arial", 20), width=5, height=2, command=lambda f=func: f(entry))\
			.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
	Button(root, text="=", font=("Arial", 24), command=lambda: eq(entry)).grid(row=5, column=5, columnspan=2, sticky="nsew")

	root.mainloop()
