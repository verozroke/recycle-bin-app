import tkinter as tk
from tkinter import PhotoImage
from generator.button import create_button
from generator.events.button import on_enter, on_leave
from functions.recycle_bin import clear_recycle_bin, update_counter
from core.colors import BACKGROUND_COLOR
from core.constants import LOGO_FILE

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Чистка корзины")
    root.geometry("600x600")
    root.config(bg=BACKGROUND_COLOR)
    root.resizable(False, False)  

    try:
        logo = PhotoImage(file=LOGO_FILE)
        root.iconphoto(False, logo)
    except Exception as e:
        print(f"Error loading logo: {e}")

    frame = tk.Frame(root, bg=BACKGROUND_COLOR)
    frame.pack(expand=True)

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    counter_label = tk.Label(frame, text="", font=("Arial", 24, "bold"), fg="#FFFFFF", bg=BACKGROUND_COLOR)
    counter_label.grid(row=0, column=0, pady=20)

    clear_button = create_button(frame, counter_label)
    clear_button.grid(row=1, column=0, pady=20)

    clear_button.bind("<Enter>", on_enter)
    clear_button.bind("<Leave>", on_leave)

    update_counter(counter_label)

    root.mainloop()

if __name__ == "__main__":
    main()
