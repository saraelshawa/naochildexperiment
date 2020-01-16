import Tkinter  as tk
from GazeFollowInteraction import GazeFollowInteraction
from naoqi import ALProxy
import time
from stand_position import stand_position
from settings import IP_ADDRESS
from settings import PORT
import tkMessageBox


#start with a jingle then gaze follow 
#maybe random jingle every time 
class GazeFollowPage(tk.Frame):
    def x(self):
        return

    def __init__(self, master, **kw):
        frame_1 = tk.Frame.__init__(self, master, **kw)
        tk.Frame.configure(self,bg='lightblue')
        tk.Label(self, text="Gaze Follow Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        gaze_following_button = tk.Button(self, text="Gaze Follow", fg="blue", command=self.gaze_follow)
        gaze_following_button.pack(side=tk.LEFT)
        self.gazeFollowInteration = GazeFollowInteraction()


    def gaze_follow(self):

        stand_position()
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
        