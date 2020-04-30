import tkinter as tk
from tkinter import ttk


def copy_text(tab, box):
    tab.clipboard_clear()
    txt = box.get()
    tab.clipboard_append(txt)


def create_clip(tab, x):
    box_label = ttk.Label(tab, text="clip" + str(x+1))
    box_label.grid(column=0, row=x, padx=10, pady=12)
    box = ttk.Entry(tab)
    box.grid(column=1, row=x, pady=5)
    copy_button = ttk.Button(tab, text="copy", command=lambda: copy_text(tab, box))
    copy_button.grid(column=2, row=x, padx=10, pady=5)
    clear_button = ttk.Button(tab, text="clear", command=lambda: box.delete(0, tk.END))
    clear_button.grid(column=3, row=x, pady=5)


def create_tool(tab, num):
    for i in range(0, num):
        create_clip(tab, i)
