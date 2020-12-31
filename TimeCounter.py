try:
    import Tkinter as tk
except:
    import tkinter as tk

import datetime

class Counter():
    def __init__(self,parent,alarmFunc):
        self.root = parent
        self.label = tk.Label(parent,text="", font=('Helvetica', 48), fg='black')
        self.label.place(x=0,y=640)

        self.Deltatime=datetime.timedelta(hours=0)
        self.timerFlag=True
        self.AlarmFunc=alarmFunc
    

    def setAlarmTime(self,time):
        self.AlarmTime=datetime.datetime.strptime ( time ,"%Y/%m/%d　%H:%M:%S")

    def start(self):
        self.update()

    def end(self):
        self.timerFlag=False


    def update(self):
        if(self.timerFlag):
            self.nowTime=datetime.datetime.now()
            time=self.AlarmTime-self.nowTime
            if(self.AlarmTime < self.nowTime):
                self.end()
                self.AlarmFunc()
                pass
            time_text=str(time)
            time_text=time_text[:-4]
            self.label.configure(text=time_text)
            self.root.after(10, self.update)
