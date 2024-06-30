import tkinter as tk
from functions.recycle_bin import update_counter, clear_recycle_bin
from core.colors import BUTTON_BACKGROUND_COLOR, BUTTON_HOVER_BACKGROUND, BUTTON_HOVER_TEXT, BUTTON_TEXT_COLOR

def on_enter(event):
    event.widget.config(bg=BUTTON_HOVER_BACKGROUND, fg=BUTTON_HOVER_TEXT, relief=tk.FLAT, bd=2)

def on_leave(event):
    event.widget.config(bg=BUTTON_BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR, relief=tk.FLAT, bd=2)
