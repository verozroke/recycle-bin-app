import tkinter as tk
from core.colors import BUTTON_BACKGROUND_COLOR, BUTTON_TEXT_COLOR
from functions.recycle_bin import clear_recycle_bin

def create_button(parent, counter_label):
    button = tk.Button(parent, text="Очистить корзину", font=("Arial", 14), bg=BUTTON_BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR, bd=0, relief=tk.FLAT, highlightthickness=0, command=lambda: clear_recycle_bin(counter_label))
    button.config(borderwidth=2, highlightbackground="#FFFFFF", relief="flat")
    return button
