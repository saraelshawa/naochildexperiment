import Tkinter  as tk
import threading 
from settings import IP_ADDRESS
from settings import PORT
from naoqi import ALProxy
import json
from settings import MOVEMENT_MAPPINGS_FILE_PATH
from sounds import sound_1, sound_2, sound_3
from stand_position import stand_position
from GazeFollowPage import GazeFollowPage
import time
import tkSimpleDialog as simpledialog


class NonSocialPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master, width=500, height=500)
        # tk.Frame.configure(self,bg='red')
        self.pack_propagate(False)

        tk.Label(self, text="Non social page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        self.textBox = tk.Text(self, height=2, width=10)
        self.textBox.pack()

        with open(MOVEMENT_MAPPINGS_FILE_PATH) as f:
                self.movement_mappings_dict = json.load(f)

        tk.Button(self, text="Retrieve input", command=lambda: self.retrieve_input()).pack()
        tk.Button(self, text="Gaze Follow Page", command=lambda: self.onEnd()).pack()
  
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
        


        self.name_of_file = "./data/nonsocial_" + self.number + "_" + self.age + "_" + self.gender 


    def retrieve_input(self):
        inputValue=self.textBox.get("1.0", "end-1c")
        print(inputValue)
        self.name_of_file += "_for_" + inputValue
        self.f = open(self.name_of_file, "w")

        log = open("./data/" + str(inputValue), "r")
        for line in log:
            timex = int(line.split(" ")[1])
            behaviour = str(line.split(" ")[0])
            print(timex)
            print(behaviour)
            timer = threading.Timer(int(timex), self.run, [str(behaviour)]) 
            timer.start() 
            self.writeToFile(behaviour, timex)
        print("this is timex" + str(timex))
        time.sleep(timex+10)
        print("Exit\n")
        self.onEnd()

    def onEnd(self):
        tk.Label(self, text="Switching to Gaze Follow", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        time.sleep(2)
        self.master.switch_frame(GazeFollowPage)

    def writeToFile(self, behaviour, timex):
        print("in write to file")
        if "/" in behaviour:
            print(behaviour)
            behaviour = self.movement_mappings_dict[behaviour]
        print(behaviour, timex)
        self.f.write('%s %s\r\n' % (behaviour, timex))

    def run(self, behaviour):
        #if behavior starts with sound 
        stand_position()
        if "sound" in str(behaviour):
            if "1" in behaviour:
                return sound_1()
            if "2" in behaviour:
                return sound_2()
            if "3" in behaviour:
                return sound_3()
        elif "left" in str(behaviour):
            print("randomly calling left")
            return self.leftKey()
        elif "right" in str(behaviour):
            print("randomly calling right")
            return self.rightKey()
        elif "up" in str(behaviour):
            print("randomly calling up")
            return self.upKey()
        elif "down" in str(behaviour):
            print("randomly calling down")
            return self.downKey()
        #else
        else:
            managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, PORT)
            managerProxy.runBehavior(str(self.movement_mappings_dict[behaviour]))

    def leftKey(self):
        print "Left key pressed"
        self.changeAngles("HeadYaw", 0.3)

    def rightKey(self):
        print "Right key pressed"
        self.changeAngles("HeadYaw", -0.3)


    def upKey(self):
        print "Up key pressed"
        # moveHead("HeadPitch", "up", 0.2, 2)
        self.changeAngles("HeadPitch", -0.15)

    def downKey(self):
        print "Down key pressed"
        self.changeAngles("HeadPitch", 0.15)


    def changeAngles(self, name, add_angle):
        motionProxy = ALProxy("ALMotion", IP_ADDRESS, PORT)
        useSensors    = True
        commandAngle = motionProxy.getAngles(name, useSensors)
        
        new_pos = [commandAngle[0] + add_angle]
        motionProxy.angleInterpolationWithSpeed([name], new_pos, 0.1)

