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
from settings import FILE_NAME
from stand_position import stand_position
import tkSimpleDialog as simpledialog

alBehaviorManagerProxy = ALProxy("ALBasicAwareness", IP_ADDRESS, PORT)
alBehaviorManagerProxy.stopAwareness()



#wave hand is to start
#peekaboo is to grab attention if the baby isn't doing anything 
class SocialPage(tk.Frame):
    def __init__(self, master, **kw):
        self.master = master
        tk.Frame.__init__(self, master, width=500, height=500)
        self.pack_propagate(False)
        # tk.Frame.configure(self, bg='red')
        self.timer = TimerApp(TIME_IN_MINUTES*60, self.onEnd, master=self) #not master so that when social page gets destroyed by switch frames, it goes as well. 
        self.timer.pack()
        self.createWidgets()
        with open(MOVEMENT_MAPPINGS_FILE_PATH) as f:
                self.movement_mappings_dict = json.load(f)

    def createWidgets(self):
        self.label = tk.Label(self, text="Social Page", font=('Helvetica', 18, "normal"))
        self.label.pack()
        
        self.wave_button = tk.Button(self, text="Wave Hand", command=self.wave)
        self.wave_button.pack() 
        
        self.make_sound_button = tk.Button(self, text="Make Sound", command=self.make_sound)
        self.make_sound_button.pack()
        
        self.movement_button = tk.Button(self, text="React to Movement", command=self.react_movement)
        self.movement_button.pack()

        self.peekaboo_button = tk.Button(self, text="Peekaboo", command=self.peekaboo)
        self.peekaboo_button.pack()



        self.left_button = tk.Button(self, text="Left ", command=self.leftKey)
        self.left_button.pack() 

        self.right_button = tk.Button(self, text="Right ", command=self.rightKey)
        self.right_button.pack() 

        self.up_button = tk.Button(self, text="Up ", command=self.upKey)
        self.up_button.pack() 

        self.down_button = tk.Button(self, text="Down", command=self.downKey)
        self.down_button.pack() 

        self.number = simpledialog.askstring("Input", "Participant number?",
                                parent=self)
        if self.number is not None:
            print("Experiment number is ", self.number)
        else:
            print("Experiment number was not inputted")

        self.age = simpledialog.askstring("Input", "Age?",
                                parent=self)
        if self.age is not None:
            print("Age is ", self.age)
        else:
            print("Age was not inputted")

        self.gender = simpledialog.askstring("Input", "Gender?",
                                parent=self)
        if self.gender is not None:
            print("Gender is ", self.gender)
        else:
            print("Gender was not inputted")
        

        

        self.name_of_file = "./data/social_" + self.number + "_" + self.age + "_" + self.gender + ".txt"
        self.f = open(self.name_of_file, "w")


        # self.bind('<Left>', self.leftKey)
        # self.bind('<Right>', self.rightKey)
        # self.bind('<Up>', self.upKey)
        # self.bind('<Down>', self.downKey)


    def wave(self):
        stand_position()
        managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, PORT)

        managerProxy.runBehavior("animations/Stand/Gestures/Hey_1") 
        self.writeToFile("animations/Stand/Gestures/Hey_1")

    def peekaboo(self):
        stand_position()
        managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, PORT)

        managerProxy.runBehavior("animations/Stand/Waiting/HideEyes_1") 
        self.writeToFile("animations/Stand/Waiting/HideEyes_1")


    def react_movement(self):
        stand_position()

        # self.writeToFile()
        print(self.movement_mappings_dict.keys())
        movement = random.choice(list(self.movement_mappings_dict.keys()))
        self.writeToFile(movement)
        print("random movement: " + str(movement))
        managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, PORT)
        managerProxy.runBehavior(str(movement))

        #get random key random.choice(list(d.keys()))

    def make_sound(self):
        stand_position()
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
    
    def leftKey(self):
        print "Left key pressed"
        self.writeToFile('left')

        self.changeAngles("HeadYaw", 0.3)
        
    def rightKey(self):
        print "Right key pressed"
        self.writeToFile('right')

        self.changeAngles("HeadYaw", -0.3)


    def upKey(self):
        print "Up key pressed"
        self.writeToFile('up')
        self.changeAngles("HeadPitch", -0.15)


    def downKey(self):
        print "Down key pressed"
        self.writeToFile('down')
        self.changeAngles("HeadPitch", 0.15)


    def changeAngles(self, name, add_angle):
        motionProxy = ALProxy("ALMotion", IP_ADDRESS, PORT)
        useSensors    = True
        commandAngle = motionProxy.getAngles(name, useSensors)
        
        new_pos = [commandAngle[0] + add_angle]
        motionProxy.angleInterpolationWithSpeed([name], new_pos, 0.1)