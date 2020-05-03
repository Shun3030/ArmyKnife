import tkinter as tk
from tkinter import ttk


def join_words(tab_name, box1, chain1, box2, chain2, box3):
    first = box1.get()
    chain1_2 = chain1.get()
    middle = box2.get()

    print(chain1_2)

    joined_word = first + chain1_2 + middle
    print(joined_word)

    tab_name.clipboard_clear()
    tab_name.clipboard_append(joined_word)


def create_joinwords(tab_name):
    chains = ['-', '_', '/']

    first_box = ttk.Entry(tab_name)
    first_box.place(relx=0.35, rely=0.2, width=200, anchor=tk.CENTER)
    f_plus_m = ttk.Label(tab_name, text=" + ")
    f_plus_m.place(relx=0.35, rely=0.3, anchor=tk.CENTER)
    middle_box = ttk.Entry(tab_name)
    middle_box.place(relx=0.35, rely=0.4, width=200, anchor=tk.CENTER)
    m_plus_l = ttk.Label(tab_name, text=" + ")
    m_plus_l.place(relx=0.35, rely=0.5, anchor=tk.CENTER)
    last_box = ttk.Entry(tab_name)
    last_box.place(relx=0.35, rely=0.6, width=200, anchor=tk.CENTER)

    chain_label1 = ttk.Label(tab_name, text="joined by")
    chain_label1.place(relx=0.75, rely=0.3, anchor=tk.CENTER)
    chain_box1 = ttk.Combobox(tab_name, values=chains, width=3)
    chain_box1.place(relx=0.9, rely=0.3, anchor=tk.CENTER)
    chain_label2 = ttk.Label(tab_name, text="joined by")
    chain_label2.place(relx=0.75, rely=0.3, anchor=tk.CENTER)
    chain_box2 = ttk.Combobox(tab_name, values=chains, width=3)
    chain_box2.place(relx=0.9, rely=0.3, anchor=tk.CENTER)

    join_button = ttk.Button(tab_name, text="copy", command=lambda: join_words(tab_name, first_box, chain_box1, middle_box, chain_box2, last_box))
    join_button.place(relx=0.8, rely=0.5, anchor=tk.CENTER)
    #result_box = ttk.Label(tab_name, text="結合結果：")
    #result_box.grid(column=1, row=3, padx=10, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("joinwords")
    root.geometry("360x250")

    create_joinwords(root)

    root.mainloop()
