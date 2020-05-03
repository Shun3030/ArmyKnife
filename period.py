import tkinter as tk
from tkinter import ttk


def gen_zfill(int_times):
    str_times = []
    for i in int_times:
        str_times.append('{:0>2}'.format(i))
    return str_times


def calc_period(start_hour, start_minute, end_hour, end_minute, result):
    try:
        start_time = int(start_hour.get()) * 60 + int(start_minute.get())
        end_time = int(end_hour.get()) * 60 + int(end_minute.get())
    
        if start_time > end_time:
            prog_time = (end_time + 1440) - start_time
        else:
            prog_time = end_time - start_time
    
        prog_hour = prog_time // 60
        prog_min = prog_time % 60

        result_text = '{:0>2}h {:0>2}m'.format(prog_hour, prog_min)
        result.configure(text=result_text)
    
    except ValueError:
        result.configure(text="error!")

        
def copy_label(tab, label):
    tab.clipboard_clear()
    txt = label.cget("text")
    tab.clipboard_append(txt)


def create_period(tab_name):
    hours = gen_zfill(list(range(24)))
    minutes = gen_zfill(list(range(60)))

    null_row = ttk.Label(tab_name, text=" ")
    null_row.grid(column=0, row=0,pady=5)

    start_hour = ttk.Combobox(tab_name, values=hours, width=3)
    start_hour.grid(column=0, row=1, padx=10, pady=20)
    start_colon = ttk.Label(tab_name, text=":")
    start_colon.grid(column=1, row=1, padx=1)
    start_minute = ttk.Combobox(tab_name, values=minutes, width=3)
    start_minute.grid(column=2, row=1, padx=10)

    progress_label = ttk.Label(tab_name, text="=> => =>")
    progress_label.grid(column=3, row=1, padx=5)

    end_hour = ttk.Combobox(tab_name, values=hours, width=3)
    end_hour.grid(column=4, row=1, padx=10, pady=5)
    end_colon = ttk.Label(tab_name, text=":")
    end_colon.grid(column=5, row=1, padx=1)
    end_minute = ttk.Combobox(tab_name, values=minutes, width=3)
    end_minute.grid(column=6, row=1, padx=10)

    calc_result = ttk.Label(tab_name, text="○○h ○○m")
    calc_result.grid(column=3, row=2, pady=10)

    calc_button = ttk.Button(tab_name, text="calc", width=7, command=lambda: calc_period(start_hour, start_minute, end_hour, end_minute, calc_result))
    calc_button.grid(column=2, row=3, pady=10)

    copy_button = ttk.Button(tab_name, text="copy", width=7, command=lambda: copy_label(tab_name, calc_result))
    copy_button.grid(column=4, row=3, pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("period")
    root.geometry("360x250")

    create_period(root)

    root.mainloop()
