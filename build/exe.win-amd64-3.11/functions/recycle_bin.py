import ctypes
from tkinter import messagebox
from core.constants import SHQUERYRBINFO

SHQueryRecycleBin = ctypes.windll.shell32.SHQueryRecycleBinW
SHEmptyRecycleBin = ctypes.windll.shell32.SHEmptyRecycleBinW

def get_recycle_bin_info():
    info = SHQUERYRBINFO()
    info.cbSize = ctypes.sizeof(SHQUERYRBINFO)
    result = SHQueryRecycleBin(None, ctypes.byref(info))
    if result != 0:
        raise ctypes.WinError(result)
    return info.i64NumItems

def update_counter(label):
    try:
        num_files = get_recycle_bin_info()
        label.config(text=f"Количество файлов в корзине: {num_files}")
    except Exception as e:
        label.config(text=f"Ошибка: {e}")

def clear_recycle_bin(counter_label):
    try:
        SHEmptyRecycleBin(None, None, 1)
        messagebox.showinfo("Успех", "Корзина очищена успешно!")
        update_counter(counter_label)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не смогли очистить вашу корзину: {e}")
