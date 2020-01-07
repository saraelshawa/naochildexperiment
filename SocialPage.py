import Tkinter  as tk
# from StartPage import StartPage
from Timer import TimerApp
from GazeFollowPage import GazeFollowPage
import time
from sounds import sound_1, sound_2, sound_3
import random 


class SocialPage(tk.Frame):


    def __init__(self, master, **kw):
        self.createWidgets()
        self.master = master
        
        tk.Frame.__init__(self, master, **kw)
        tk.Frame.configure(self,bg='lightblue')
        timer = TimerApp(9, self.onEnd, master=self) #not master so that when social page gets destroyed by switch frames, it goes as well. 
        timer.pack()
        # print(timer.returnCurrentTime())
    
    def createWidgets(self):
        tk.Label(self, text="Social Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Make Sound", command=self.make_sound()).pack()
        tk.Button(self, text="React to Movement", command=None).pack()
        tk.Button(self, text="Wave hand", command=None).pack()
        
    def make_sound(self):
        # stand_position()
        x = random.choice([0, 1, 2])
        print("x is " + str(x))
        if x == 0:
            return sound_1()
        if x == 1: 
            return sound_2()
        if x == 2:
            return sound_3()

    def onEnd(self):
        tk.Label(self, text="Switching to Gaze Follow", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        time.sleep(2)
        self.master.switch_frame(GazeFollowPage)
