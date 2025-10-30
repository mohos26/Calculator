"""
28.08.2025
"""

import tkinter as tk
from tkinter import ttk
from buttons import buttons
from eq import eq
from events import events

# --- Style Configuration ---
STYLE = {
    "BG_WINDOW": "#2E2E2E",
    "BG_DISPLAY": "#4A4A4A",
    "FG_DISPLAY": "#FFFFFF",
    "BG_OPERATOR": "#FF9500",
    "FG_OPERATOR": "#FFFFFF",
    "BG_SPECIAL": "#D4D4D2",
    "FG_SPECIAL": "#000000",
    "BG_NUMPAD": "#505050",
    "FG_NUMPAD": "#FFFFFF",
    "FONT_DISPLAY": ("Noto Sans", 38, "bold"),
    "FONT_BUTTON": ("Noto Sans", 18, "bold"),
}

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.configure(bg=STYLE["BG_WINDOW"])
        self.setup_window()
        self.configure_grid()
        self.create_styles()
        self.create_display()
        self.create_buttons()
        events(self.root, self.entry)
        self.root.focus_set()

    def setup_window(self):
        window_width = 700
        window_height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.minsize(window_width, window_height)
        self.root.maxsize(window_width, window_height)

    def configure_grid(self):
        for i in range(7):
            self.root.grid_columnconfigure(i, weight=1)
        for j in range(6):
            self.root.grid_rowconfigure(j, weight=1)

    def create_styles(self):
        style = ttk.Style()
        style.theme_use("clam")  # أفضل ثيم لـ Linux

        # الأسلوب العام للأزرار
        style.configure(
            "TButton",
            font=STYLE["FONT_BUTTON"],
            relief="flat",
            borderwidth=0,
            padding=10,
            anchor="center",
        )

        # أنواع الأزرار
        style.configure("Num.TButton", background=STYLE["BG_NUMPAD"], foreground=STYLE["FG_NUMPAD"])
        style.map("Num.TButton", background=[("active", "#606060")])

        style.configure("Op.TButton", background=STYLE["BG_OPERATOR"], foreground=STYLE["FG_OPERATOR"])
        style.map("Op.TButton", background=[("active", "#FFB84D")])

        style.configure("Spec.TButton", background=STYLE["BG_SPECIAL"], foreground=STYLE["FG_SPECIAL"])
        style.map("Spec.TButton", background=[("active", "#E6E6E6")])

    def create_display(self):
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(
            self.root,
            textvariable=self.entry_var,
            font=STYLE["FONT_DISPLAY"],
            justify="right",
            state="readonly",
        )
        self.entry.grid(
            row=0,
            column=0,
            columnspan=7,
            padx=10,
            pady=10,
            sticky="nsew",
            ipady=20
        )

        # ضبط اللون يدويًا لأن ttk.Entry لا يدعم bg بسهولة
        self.entry.configure(style="Display.TEntry")
        style = ttk.Style()
        style.configure(
            "Display.TEntry",
            fieldbackground=STYLE["BG_DISPLAY"],
            foreground=STYLE["FG_DISPLAY"]
        )

    def get_button_style(self, text):
        if text.isdigit() or text == ".":
            return "Num.TButton"
        if text in "+-*/":
            return "Op.TButton"
        if text in "C±%DEL":
            return "Spec.TButton"
        return "Num.TButton"

    def create_buttons(self):
        for (text, row, col, func) in buttons:
            style_name = self.get_button_style(text)
            ttk.Button(
                self.root,
                text=text,
                style=style_name,
                command=lambda f=func, e=self.entry: f(e)
            ).grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

        ttk.Button(
            self.root,
            text="=",
            style="Op.TButton",
            command=lambda: eq(self.entry)
        ).grid(row=5, column=5, columnspan=2, padx=1, pady=1, sticky="nsew")

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
