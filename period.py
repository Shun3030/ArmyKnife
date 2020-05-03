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
        result.configure(text=result_text, font=("",15))
    
    except ValueError:
        result.configure(text="error!", font=("",15), foreground='#ff0000')

        
def copy_label(tab, label):
    tab.clipboard_clear()
    txt = label.cget("text")
    tab.clipboard_append(txt)


def create_period(tab_name):
    hours = gen_zfill(list(range(24)))
    minutes = gen_zfill(list(range(60)))

    start_label = ttk.Label(tab_name, text='start time')
    start_label.place(relx=0.25, rely=0.15, anchor=tk.CENTER)

    start_hour = ttk.Combobox(tab_name, values=hours, width=3)
    start_hour.place(relx=0.15, rely=0.25, anchor=tk.CENTER)
    start_colon = ttk.Label(tab_name, text=":")
    start_colon.place(relx=0.25, rely=0.25, anchor=tk.CENTER)
    start_minute = ttk.Combobox(tab_name, values=minutes, width=3)
    start_minute.place(relx=0.35, rely=0.25, anchor=tk.CENTER)

    progress_label = ttk.Label(tab_name, text="=>", font=("",12))
    progress_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    end_label = ttk.Label(tab_name, text='end time')
    end_label.place(relx=0.75, rely=0.15, anchor=tk.CENTER)

    end_hour = ttk.Combobox(tab_name, values=hours, width=3)
    end_hour.place(relx=0.65, rely=0.25, anchor=tk.CENTER)
    end_colon = ttk.Label(tab_name, text=":")
    end_colon.place(relx=0.75, rely=0.25, anchor=tk.CENTER)
    end_minute = ttk.Combobox(tab_name, values=minutes, width=3)
    end_minute.place(relx=0.85, rely=0.25, anchor=tk.CENTER)

    calc_result = ttk.Label(tab_name, text="○○h ○○m", font=("",15))
    calc_result.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    calc_button = ttk.Button(tab_name, text="calc", width=7, command=lambda:\
         calc_period(start_hour, start_minute, end_hour, end_minute, calc_result))
    calc_button.place(relx=0.3, rely=0.8, anchor=tk.CENTER)

    copy_button = ttk.Button(tab_name, text="copy", width=7, command=lambda:\
         copy_label(tab_name, calc_result))
    copy_button.place(relx=0.7, rely=0.8, anchor=tk.CENTER)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("period")
    root.geometry("360x250")

    create_period(root)

    root.mainloop()
