import tkinter as tk
from tkinter import ttk
from plyer import notification
import period


class Timer:
    def __init__(self, tab_name, min, sec, label):
        self.tab = tab_name
        self.min = min
        self.sec = sec
        self.minsec = 0
        self.label = label
        self.count = False

    def set_timer(self, min, sec):
        try:
            self.min = int(min)
            self.sec = int(sec)
            if 0 <= self.sec < 60 and 0 <= self.min < 100:
                self.minsec = self.min * 60 + self.sec
                self.label.configure(text='{:0>2}:{:0>2}'.format(self.min, self.sec), font=("",50), foreground='#000000')
                #print(f'set_timer() has completed! minsec={self.minsec} count={self.count}') # デバッグ用
            elif self.sec < 0 or 60 <= self.sec:
                self.label.configure(text='sec range is 0~59', font=("",30), foreground='#ff0000')
                self.count == False
            elif self.min < 0 or 100 <= self.min:
                self.label.configure(text='min range is 0~99', font=("",30), foreground='#ff0000')
                self.count == False
            else:
                self.label.configure(text='FatalError!', font=("",50), foreground='#ff0000')
                self.count == False
        except ValueError:
            self.label.configure(text='ValueError!', font=("",50), foreground='#ff0000')
            self.count == False
        
    def start_timer(self):
        if self.count == False:
            self.count = True
            self.timer_refresh()
        #notify('timer is running!')
        #print(f'timer is running! minsec={self.minsec} count={self.count}') # デバッグ用

    def timer_refresh(self):
        if self.minsec > 0 and self.count == True:
            self.tab.after(1000, self.timer_refresh)
            self.minsec -= 1
            self.min = self.minsec // 60
            self.sec = self.minsec % 60
            self.label.configure(text='{:0>2}:{:0>2}'.format(self.min, self.sec), font=("",50), foreground='#000000')

        #if self.minsec > 0 and self.count == False:
            #notify('timer has stopped!')
            #print(f'timer has stopped! minsec={self.minsec} count={self.count}') # デバッグ用    
        
        if self.minsec == 0 and self.count == True:
            notify('timer has finished!')
            self.clear_timer()
            #print('timer_refresh() has completed!') # デバッグ用

    def timer_stop(self):
        self.count = False
    
    def clear_timer(self):
        self.minsec = 0
        self.count = False
        self.label.configure(text='00:00', font=("",50), foreground='#000000')
        #print(f'clear_timer() has complited! minsec={self.minsec} count={self.count}') # デバッグ用


def notify(message):
    notification.notify(
            title='ArmyKnife timer',
            message=message,
            app_name='ArmyKnife',
            app_icon='./armyknife.ico'
        )


def create_timer(tab_name):
    min_list = period.gen_zfill(list(range(31)))
    sec_list = period.gen_zfill(list(range(60)))

    min_label = ttk.Label(tab_name, text="mm")
    min_label.place(relx=0.25, rely=0.1, anchor=tk.CENTER)
    sec_label = ttk.Label(tab_name, text="ss")
    sec_label.place(relx=0.75, rely=0.1, anchor=tk.CENTER)

    min_box = ttk.Combobox(tab_name, values=min_list, width=4)
    min_box.place(relx=0.25, rely=0.2, anchor=tk.CENTER)
    sec_box = ttk.Combobox(tab_name, values=sec_list, width=4)
    sec_box.place(relx=0.75, rely=0.2, anchor=tk.CENTER)

    timer_label = ttk.Label(tab_name, text="00:00", font=("",50))
    timer_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    timer = Timer(tab_name, 0, 0, timer_label)

    set_button = ttk.Button(tab_name, text="set", width=7, command=lambda: timer.set_timer(min_box.get(), sec_box.get()))
    set_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    start_button = ttk.Button(tab_name, text="start", width=7, command=timer.start_timer)
    start_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    stop_button = ttk.Button(tab_name, text="stop", width=7, command=timer.timer_stop)
    stop_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    clear_button = ttk.Button(tab_name, text="clear", width=3.5, command=timer.clear_timer)
    clear_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("timer")
    root.geometry("360x250")
    
    create_timer(root)

    root.mainloop()
