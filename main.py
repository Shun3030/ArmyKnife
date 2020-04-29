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


    # multiclipタブの作成
    tab_multiclip = create_tab('multiclip')
    for i in range(0, 5):
        multiclip.create_clip(tab_multiclip, i)


    # テスト用タブ
    create_tab('test')

    
    root.mainloop()