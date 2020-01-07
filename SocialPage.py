import Tkinter  as tk
from Timer import TimerApp
from GazeFollowPage import GazeFollowPage
import time
from sounds import sound_1, sound_2, sound_3
import random 

class SocialPage(tk.Frame):
    def __init__(self, master, **kw):
        self.master = master
        self.f = open("examplefile.txt", "a+")
        tk.Frame.__init__(self, master, **kw)
        tk.Frame.configure(self,bg='lightblue')
        self.timer = TimerApp(20, self.onEnd, master=self) #not master so that when social page gets destroyed by switch frames, it goes as well. 
        self.timer.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label = tk.Label(self, text="Social Page", font=('Helvetica', 18, "bold"))
        self.label.pack()
        
        self.make_sound_button = tk.Button(self, text="Make Sound", command=self.make_sound)
        self.make_sound_button.pack()
        
        self.movement_button = tk.Button(self, text="React to Movement", command=self.react_movement)
        self.movement_button.pack()

        self.wave_button = tk.Button(self, text="Wave hand", command=self.timer.returnCurrentTime)
        self.wave_button.pack()

    def react_movement(self):
        self.writeToFile("movement")

    def make_sound(self):
        print("in make sound")
        # stand_position()
        x = random.choice([0, 1, 2])
        print("x is " + str(x))
        self.writeToFile("sound_1")
        
    def onEnd(self):
        tk.Label(self, text="Switching to Gaze Follow", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        time.sleep(2)
        self.master.switch_frame(GazeFollowPage)

    def writeToFile(self, movement):
        print("in write to file")
        self.f.write('%s %s\r\n' % (movement, self.timer.current))