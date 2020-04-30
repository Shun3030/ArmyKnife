import tkinter as tk
from tkinter import ttk

import multiclip, period


def create_tab(name):
    tab = tk.Frame(nb)
    nb.add(tab, text=name, padding=3)
    return tab
    

if __name__ == '__main__':
    root = tk.Tk()
    root.title("ArmyKnife")
    root.geometry("360x250")
    nb = ttk.Notebook(root)
    nb.pack(expand=1, fill="both")

    multiclip.create_multiclip(create_tab('multiclip'), 5)
    period.create_period(create_tab('period'))

    root.mainloop()