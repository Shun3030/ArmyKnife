import tkinter as tk
from tkinter import ttk, messagebox

import multiclip, period, passgen, joinwords, timer, reminder


def create_tab(name):
    tab = tk.Frame(nb)
    nb.add(tab, text=name, padding=3)
    return tab

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
    

if __name__ == '__main__':
    root = tk.Tk()
    root.title("ArmyKnife")
    root.geometry("360x250")
    root.resizable(width=False, height=False)
    nb = ttk.Notebook(root)
    nb.pack(expand=1, fill="both")
    iconfile = './armyknife.ico'
    root.iconbitmap(default=iconfile)

    multiclip.create_multiclip(create_tab('multiclip'), 5)
    joinwords.create_joinwords(create_tab('joinwords'))
    period.create_period(create_tab('period'))
    passgen.create_passgen(create_tab('passgen'))
    timer.create_timer(create_tab('timer'))
    reminder.create_reminder(create_tab('reminder'))

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()