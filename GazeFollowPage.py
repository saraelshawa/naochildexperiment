import Tkinter  as tk
from GazeFollowInteraction import GazeFollowInteraction
from naoqi import ALProxy
import time
from stand_position import stand_position
from settings import IP_ADDRESS
from settings import PORT
import tkMessageBox
import random 


#start with a jingle then gaze follow 
#maybe random jingle every time 
class GazeFollowPage(tk.Frame):
    def x(self):
        return

    def __init__(self, master, **kw):
        # frame_1 = tk.Frame.__init__(self, master, **kw)
        tk.Frame.__init__(self, master, width=500, height=500)
        self.pack_propagate(False)

        # tk.Frame.configure(self,bg='lightblue')
        tk.Label(self, text="Gaze Follow Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        gaze_following_button = tk.Button(self, text="Gaze Follow", fg="blue", command=self.gaze_follow)
        gaze_following_button.pack(side=tk.LEFT)
        self.gazeFollowInteration = GazeFollowInteraction()

        grab_attention_button = tk.Button(self, text="Grab Attention", fg="blue", command=self.grab_attention)
        grab_attention_button.pack(side=tk.RIGHT)


    def gaze_follow(self):

        stand_position()
        #choose random jingle sound 
        self.play_sound()
        time.sleep(2)
        next_move = self.gazeFollowInteration.get_next_move()
        if next_move == GazeFollowInteraction.LEFT_HEAD_MOVE:
            self.move_head_diagonal(0.45, 0.45)
        elif next_move == GazeFollowInteraction.RIGHT_HEAD_MOVE:
            self.move_head_diagonal(0.45, -0.45)
        
        elif next_move == "6/6 done":
            print("alll doneee")
            tkMessageBox.showinfo("End of Experiment", "6/6 gaze following done")
        #hold for 5 seconds
        time.sleep(5)
        stand_position()
        return
    
    def move_head_diagonal(self, angle_up_down, angle_left_right):
        motionProxy = ALProxy("ALMotion", IP_ADDRESS, PORT)

        angleLists = [angle_up_down, angle_left_right]
        timeLists = [1,1]
        isAbsolute  = True
        motionProxy.angleInterpolation(["HeadPitch", "HeadYaw"], angleLists, timeLists, isAbsolute)
    
    def play_sound(self):
        managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, PORT)
        x = random.choice([0, 1, 2])
        print("x is " + str(x))
        if x == 0:
            managerProxy.runBehavior('untitled-1fb4c9/ding-ding')
        if x == 1: 
            managerProxy.runBehavior('untitled-e2cddf/game_fail_sound')
        if x == 2:
            managerProxy.runBehavior('untitled-dabbc5/sleigh_bell_sound')
    
    def grab_attention(self):
        managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, PORT)

        managerProxy.runBehavior('untitled-c05a30/game_win_sound') #grab attention 


        # 'untitled-1fb4c9/ding-ding', 'untitled-e2cddf/game_fail_sound', 'untitled-c05a30/game_win_sound', 'untitled-dabbc5/sleigh_bell_sound'
