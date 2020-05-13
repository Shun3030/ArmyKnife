import tkinter as tk
from tkinter import ttk
from plyer import notification
import datetime as dt
import period, timer


class Reminder:
    def __init__(self, box_hour, box_min, box_bln, box_desc):
        self.box_hour = box_hour
        self.box_min = box_min
        self.box_bln = box_bln
        self.box_desc = box_desc
    
    def alert(self):
        if self.box_bln.get() == True:
            try:
                hour = int(self.box_hour.get())
                min = int(self.box_min.get())
                now= dt.datetime.now()
                if hour == now.hour and min == now.minute:
                    description = self.box_desc.get()
                    if description == '':
                        description = "It\'s time to start!"
                    print(description)
                    timer.notify('ArmyKnife reminder', description)
                    self.box_bln.set(False)
            except ValueError:
                self.box_bln.set(False)


def run_reminder(tab, status, rmds):
    if status.cget('text') == 'Reminder is running':
        tab.after(1000, lambda: run_reminder(tab, status, rmds))
        # print('running...')
        for rmd in rmds:
            rmd.alert()
    else:
        # print('stopped!')
        pass
        

def start_reminder(tab, status, rmds):
    if status.cget('text') == 'Reminder is stopping':
        status.configure(text='Reminder is running', font=("",20), foreground='#ff0000')
        run_reminder(tab, status, rmds)


def stop_reminder(tab, status):
    status.configure(text='Reminder is stopping', font=("",20), foreground='#000000')


def create_reminder(tab_name):
    hour_list = period.gen_zfill(list(range(24)))
    min_list = period.gen_zfill(list(range(60)))

    # 最上段のラベル
    top_hour_label = ttk.Label(tab_name, text='hh')
    top_hour_label.place(relx=0.1, rely=0.1, anchor=tk.CENTER)
    top_min_label = ttk.Label(tab_name, text='mm')
    top_min_label.place(relx=0.25, rely=0.1, anchor=tk.CENTER)
    desc_label = ttk.Label(tab_name, text='description', width=10)
    desc_label.place(relx=0.6, rely=0.1, anchor=tk.CENTER)
    set_label = ttk.Label(tab_name, text='set')
    set_label.place(relx=0.9, rely=0.1, anchor=tk.CENTER)

    # reminder1
    hour_box1 = ttk.Combobox(tab_name, values=hour_list, width=2)
    hour_box1.place(relx=0.1, rely=0.2, anchor=tk.CENTER)
    colon_label1 = ttk.Label(tab_name, text=':') 
    colon_label1.place(relx=0.175, rely=0.2, anchor=tk.CENTER)
    min_box1 = ttk.Combobox(tab_name, values=min_list, width=2)
    min_box1.place(relx=0.25, rely=0.2, anchor=tk.CENTER)
    desc_box1 = ttk.Entry(tab_name)
    desc_box1.place(relx=0.6, rely=0.2, anchor=tk.CENTER, width=180)
    bln1 = tk.BooleanVar()
    bln1.set(False)
    set_chkbtn1 = ttk.Checkbutton(tab_name, variable=bln1, text='')
    set_chkbtn1.place(relx=0.91, rely=0.2, anchor=tk.CENTER)

    # reminder2
    hour_box2 = ttk.Combobox(tab_name, values=hour_list, width=2)
    hour_box2.place(relx=0.1, rely=0.35, anchor=tk.CENTER)
    colon_label2 = ttk.Label(tab_name, text=':') 
    colon_label2.place(relx=0.175, rely=0.35, anchor=tk.CENTER)
    min_box2 = ttk.Combobox(tab_name, values=min_list, width=2)
    min_box2.place(relx=0.25, rely=0.35, anchor=tk.CENTER)
    desc_box2 = ttk.Entry(tab_name)
    desc_box2.place(relx=0.6, rely=0.35, anchor=tk.CENTER, width=180)
    bln2 = tk.BooleanVar()
    bln2.set(False)
    set_chkbtn1 = ttk.Checkbutton(tab_name, variable=bln2, text='')
    set_chkbtn1.place(relx=0.91, rely=0.35, anchor=tk.CENTER)

    # reminder3
    hour_box3 = ttk.Combobox(tab_name, values=hour_list, width=2)
    hour_box3.place(relx=0.1, rely=0.5, anchor=tk.CENTER)
    colon_label3 = ttk.Label(tab_name, text=':') 
    colon_label3.place(relx=0.175, rely=0.5, anchor=tk.CENTER)
    min_box3 = ttk.Combobox(tab_name, values=min_list, width=2)
    min_box3.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
    desc_box3 = ttk.Entry(tab_name)
    desc_box3.place(relx=0.6, rely=0.5, anchor=tk.CENTER, width=180)
    bln3 = tk.BooleanVar()
    bln3.set(False)
    set_chkbtn3 = ttk.Checkbutton(tab_name, variable=bln3, text='')
    set_chkbtn3.place(relx=0.91, rely=0.5, anchor=tk.CENTER)

    # ON/OFF 制御
    btn_on = ttk.Button(tab_name, text='on', width=7, command=lambda: start_reminder(tab_name, status, reminders))
    btn_on.place(relx=0.85, rely=0.75, anchor=tk.CENTER)
    btn_off = ttk.Button(tab_name, text='off', width=7, command=lambda: stop_reminder(tab_name, status))
    btn_off.place(relx=0.85, rely=0.9, anchor=tk.CENTER)
    status = ttk.Label(tab_name, text='Reminder is stopping', font=("",20))
    status.place(relx=0.38, rely=0.8, anchor=tk.CENTER)

    # reminderインスタンス作成
    rmd1 = Reminder(hour_box1, min_box1, bln1, desc_box1)
    rmd2 = Reminder(hour_box2, min_box2, bln2, desc_box2)
    rmd3 = Reminder(hour_box3, min_box3, bln3, desc_box3)

    reminders = [rmd1, rmd2, rmd3]


if __name__ == '__main__':
    root = tk.Tk()
    root.title("reminder")
    root.geometry("360x250")
    
    create_reminder(root)

    root.mainloop()
