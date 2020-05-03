import tkinter as tk
from tkinter import ttk
import string, secrets


upp_letters = string.ascii_uppercase
low_letters = string.ascii_lowercase
digits = string.digits
symbols = '!"#$%&\')(=~|-^@`][}{;:+*,.></?_'
exclude_letters = ['0', 'O', 'l', 'I', '1']


def pass_gen(size, sym_flag):
    chars = upp_letters + low_letters + digits
    if sym_flag == True:
        chars += symbols
    for word in exclude_letters:
        chars = chars.replace(word, '')
    password = ''.join(secrets.choice(chars) for x in range(size))
    #print(password)
    return password


def pass_check(password, sym_flag):
    for dig in digits:
        if dig in password:
            break
    else:
        #print('dig not in pass')
        return True
    
    for upp in upp_letters:
        if upp in password:
            break
    else:
        #print('upp not in pass')
        return True
    
    for low in low_letters:
        if low in password:
            break
    else:
        #print('low not in pass')
        return True

    if sym_flag == True:
        for sym in symbols:
            if sym in password:
                break
        else:
            #print('sym not in pass')
            return True
    
    return False


def pass_decide(size, sym_flag, pass_label):
    try:
        size = int(size)
        if 3 < size < 100:
            check_flag = True
            while check_flag:
                password = pass_gen(size, sym_flag)
                check_flag = pass_check(password, sym_flag)
            #print(password)
            pass_label.configure(text=password, font=("",20), foreground='#000000')
        else:
            pass_label.configure(text='ERROR: The number of characters is out of range.', font=("",12), foreground='#ff0000')
    except ValueError:
        pass_label.configure(text='ERROR: Enter the number of characters.', font=("",12), foreground='#ff0000')


def copy_label(tab, label):
    tab.clipboard_clear()
    txt = label.cget("text")
    tab.clipboard_append(txt)


def create_passgen(tab_name):
    null_column0 = ttk.Label(tab_name, text=" ")
    null_column0.grid(column=0, row=0, padx=10, pady=30)

    size_box = ttk.Entry(tab_name, width=3)
    size_box.insert(tk.END, 10)
    size_box.grid(column=1, row=0, padx=5)
    size_label = ttk.Label(tab_name, text='characters (4~99)')
    size_label.grid(column=2, row=0)

    null_column3 = ttk.Label(tab_name, text=" ")
    null_column3.grid(column=3, row=0, padx=20)

    bln = tk.BooleanVar()
    bln.set(True)
    symflag_chkbtn = ttk.Checkbutton(tab_name, variable=bln, text='use symbol')
    symflag_chkbtn.grid(column=4, row=0, padx=5)

    pass_label = ttk.Label(tab_name, text='Press "generate" buttun', font=("",12), foreground='#000000')
    pass_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    gen_button = ttk.Button(tab_name, text="generate", command=lambda: pass_decide(size_box.get(), bln.get(), pass_label))
    gen_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    copy_button = ttk.Button(tab_name, text="copy", command=lambda: copy_label(tab_name, pass_label))
    copy_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("passgen")
    root.geometry("360x250")

    create_passgen(root)

    root.mainloop()
