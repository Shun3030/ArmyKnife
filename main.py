import tkinter as tk
from tkinter import ttk

import multiclip


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

    # multiclipタブの作成(第二引数でクリップボードの個数を指定)
    multiclip.create_tool(create_tab('multiclip'), 5)


    # テスト用タブ
    create_tab('test1')
    create_tab('test2')

    
    root.mainloop()