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

class NonSocialPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Non social page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        self.textBox = tk.Text(self, height=2, width=10)
        self.textBox.pack()

        with open(MOVEMENT_MAPPINGS_FILE_PATH) as f:
                self.movement_mappings_dict = json.load(f)

        tk.Button(self, text="Retrieve input", command=lambda: self.retrieve_input()).pack()
        tk.Button(self, text="Gaze Follow Page", command=lambda: self.onEnd()).pack()

    def retrieve_input(self):
        inputValue=self.textBox.get("1.0", "end-1c")
        print(inputValue)

        log = open("./data/" + str(inputValue), "r")
        for line in log:
            timex = int(line.split(" ")[1])
            behavior = str(line.split(" ")[0])
            print(timex)
            print(behavior)
            timer = threading.Timer(int(timex), self.run, [str(behavior)]) 
            timer.start() 
        print("this is timex" + str(timex))
        time.sleep(timex+10)
        print("Exit\n")
        self.onEnd()

    def onEnd(self):
        tk.Label(self, text="Switching to Gaze Follow", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        time.sleep(2)
        self.master.switch_frame(GazeFollowPage)



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
# 
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

