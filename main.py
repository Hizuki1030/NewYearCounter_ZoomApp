import tkinter as tk
from tkinter import ttk
import cv2
from PIL import ImageTk, Image
from tkinter import font
import time
import TimeCounter

class Application(tk.Frame):
    def __init__(self,master, video_source=0):
        super().__init__(master)
        self.master.title("Tkinter with Video Streaming and Capture")
        self.PictureEventFlag=False
        # ---------------------------------------------------------
        # Open the video source
        # ---------------------------------------------------------

        self.vcap = cv2.VideoCapture( video_source )
        self.width = self.vcap.get( cv2.CAP_PROP_FRAME_WIDTH )
        self.height = self.vcap.get( cv2.CAP_PROP_FRAME_HEIGHT )

        # ---------------------------------------------------------
        # Widget
        # ---------------------------------------------------------

        self.create_widgets()
        self.TimerApp=TimeCounter.Counter(self.master,self.Alarm)
        self.TimerApp.setAlarmTime("2021/1/1 0:0:0")
        self.TimerApp.start()
        # ---------------------------------------------------------
        # Canvas Update
        # ---------------------------------------------------------

        self.delay = 15 #[mili seconds]
        self.update()


    def create_widgets(self):
        #Canvas
        self.canvas1 = tk.Canvas()
        self.canvas1.configure( width= self.width, height=self.height,bg="white")
        self.canvas1.pack()
    
    def update(self):
        #self.TimerApp.update()
        #Get a frame from the video source
        _, frame = self.vcap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #self.photo -> Canvas

        if(self.PictureEventFlag):
            print(self.PictureEventFlag)
            image = cv2.imread("picture/happynewyear.png")
            image=cv2.bitwise_not(image)

            height_image, width_image = image.shape[:2]
            height_frame, width_frame = frame.shape[:2]

            height_start=int(height_frame/2 - height_image/2)
            width_start=int(width_frame/2 - height_image/2)

            height_end=int(height_start + height_image)
            width_end=int(width_start + width_image)
            frame[height_start:height_end, width_start:width_end] = image
        self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
        self.canvas1.create_image(0,0, image= self.photo, anchor = tk.NW)



        self.master.after(self.delay, self.update)   
    def Alarm(self):
        print("changed")
        self.PictureEventFlag=True



def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()



