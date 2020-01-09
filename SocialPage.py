import Tkinter  as tk
from Timer import TimerApp
from naoqi import ALProxy    
import qi
from GazeFollowPage import GazeFollowPage
from settings import IP_ADDRESS
from settings import PORT
from settings import MOVEMENT_MAPPINGS_FILE_PATH
from settings import TIME_IN_MINUTES
import time
from sounds import sound_1, sound_2, sound_3
import random 
import json
from stand_position import stand_position




alBehaviorManagerProxy = ALProxy("ALBasicAwareness", IP_ADDRESS, PORT)
alBehaviorManagerProxy.stopAwareness()

class SocialPage(tk.Frame):
    def __init__(self, master, **kw):
        self.master = master
        self.f = open("examplefile.txt", "a+")
        tk.Frame.__init__(self, master, **kw)
        tk.Frame.configure(self,bg='lightblue')
        self.timer = TimerApp(TIME_IN_MINUTES*60, self.onEnd, master=self) #not master so that when social page gets destroyed by switch frames, it goes as well. 
        self.timer.pack()
        self.createWidgets()
        with open(MOVEMENT_MAPPINGS_FILE_PATH) as f:
                self.movement_mappings_dict = json.load(f)

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
        # stand_position()

        # self.writeToFile()
        print(self.movement_mappings_dict.keys())
        movement = random.choice(list(self.movement_mappings_dict.keys()))
        self.writeToFile(movement)
        print("random movement: " + str(movement))
        managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, PORT)
        managerProxy.runBehavior("animations/Stand/Gestures/" + str(movement))

        #get random key random.choice(list(d.keys()))

    def make_sound(self):
        print("in make sound")
        stand_position()
        x = random.choice([0, 1, 2])
        print("x is " + str(x))
        self.writeToFile("sound_" + str(x))
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

    def writeToFile(self, movement):
        print("in write to file")
        self.f.write('%s %s\r\n' % (movement, self.timer.current))