import Tkinter  as tk
from naoqi import ALProxy    
from sys import exit
import qi
import time
from settings import IP_ADDRESS
from blink import blink 
import random 

from GazeFollowInteraction import GazeFollowInteraction
from hand_wave import hand_wave
from gangam_style import gangam_style_position, gangam_style_dance
from stand_position import stand_position
from sounds import sound_1, sound_2, sound_3


alBehaviorManagerProxy = ALProxy("ALBasicAwareness", IP_ADDRESS, 9559)
alBehaviorManagerProxy.stopAwareness()	


def quit():
    global root
    root.quit()


def eye_color():
    session = qi.Session()
    session.connect("tcp://" + IP_ADDRESS + ":9559")
    leds_service = session.service("ALLeds")

    # Example showing how to fade the eyes to green 
    stand_position()
    name = 'FaceLeds'
    leds_service.rasta(2)


def moveHead(type, direction, angle, time_end):
    motionProxy = ALProxy("ALMotion", IP_ADDRESS, 9559)

    #left or right
    if type == "HeadYaw":
        if direction == "left":
            angleLists = [[angle]*time_end]
        if direction == "right":
            angleLists = [[-angle]*time_end]
        timeLists = [range(1, time_end+1)]
        print(angleLists, timeLists)
        isAbsolute  = True
        motionProxy.angleInterpolation(["HeadYaw"], angleLists, timeLists, isAbsolute)
    
    #up or down 
    if type == "HeadPitch":
        if direction == "up":
            angleLists = [[-angle]*time_end]
        if direction == "down":
            angleLists = [[angle]*time_end]
        timeLists = [range(1, time_end+1)]
        isAbsolute  = True
        motionProxy.angleInterpolation(["HeadPitch"], angleLists, timeLists, isAbsolute)


def make_sound():
    stand_position()
    x = random.choice([0, 1, 2])
    print("x is " + str(x))
    if x == 0:
        return sound_1()
    if x == 1: 
        return sound_2()
    if x == 2:
        return sound_3()


def move_head_diagonal(angle_up_down, angle_left_right):
    motionProxy = ALProxy("ALMotion", IP_ADDRESS, 9559)

    angleLists = [angle_up_down, angle_left_right]
    timeLists = [1,1]
    isAbsolute  = True
    motionProxy.angleInterpolation(["HeadPitch", "HeadYaw"], angleLists, timeLists, isAbsolute)
   



gazeFollowInteration = GazeFollowInteraction()
def gaze_follow():
    stand_position()
    next_move = gazeFollowInteration.get_next_move()
    if next_move == GazeFollowInteraction.LEFT_HEAD_MOVE:
        move_head_diagonal(0.45, 0.45)
    elif next_move == GazeFollowInteraction.RIGHT_HEAD_MOVE:
        move_head_diagonal(0.45, -0.45)
    
    #hold for 5 seconds
    time.sleep(5)
    stand_position()

    return


def dance():
    stand_position()
    managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, 9559)
    managerProxy.runBehavior('gangnamstyle4-9610b3/GangnamStyle')


def hand_wave_func():
    stand_position()
    managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, 9559)
    managerProxy.runBehavior("animations/Stand/Gestures/Hey_1")
    # tts = ALProxy("ALAnimationPlayer", IP_ADDRESS, 9559)
    # tts.run("animations/Stand/Gestures/Hey_1!")

def come_on_func():
    stand_position()
    managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, 9559)

    managerProxy.runBehavior("animations/Stand/Gestures/ComeOn_1")


def changeAngles(name, add_angle):
    motionProxy = ALProxy("ALMotion", IP_ADDRESS, 9559)
    useSensors    = True
    commandAngle = motionProxy.getAngles(name, useSensors)
    
    new_pos = [commandAngle[0] + add_angle]
    motionProxy.angleInterpolationWithSpeed([name], new_pos, 0.1)

def random_reaction():
    x = random.choice([0, 1, 2])
    print("x is " + str(x))
    if x == 0:
        return hand_wave_func()
    if x == 1: 
        return eye_color()
    if x == 2: 
        return come_on_func()


root = tk.Tk()
root.geometry("500x500")
frame = tk.Frame(root)
frame.pack()
root.protocol('WM_DELETE_WINDOW', root.quit())


button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)

eye_button = tk.Button(frame, text="React to Movement", fg="red", command=random_reaction)
eye_button.pack(side=tk.LEFT)

sound_button = tk.Button(frame, text="Make Sound", fg="red", command=make_sound)
sound_button.pack(side=tk.RIGHT)

gaze_following_button = tk.Button(frame, text="Gaze Follow", fg="blue", command=gaze_follow)
gaze_following_button.pack(side=tk.LEFT)

play_dance_button = tk.Button(frame, text="Dance", fg="blue", command=dance)
play_dance_button.pack(side=tk.LEFT)

wave_hand_button = tk.Button(frame, text="Wave hand", fg="blue", command=hand_wave_func)
wave_hand_button.pack(side=tk.LEFT)


def leftKey(event):
    print "Left key pressed"
    changeAngles("HeadYaw", 0.3)


def rightKey(event):
    print "Right key pressed"
    changeAngles("HeadYaw", -0.3)

def upKey(event):
    print "Up key pressed"
    # moveHead("HeadPitch", "up", 0.2, 2)
    changeAngles("HeadPitch", -0.15)

def downKey(event):
    print "Down key pressed"
    changeAngles("HeadPitch", 0.15)

root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)

root.mainloop()

def get_behaviours():
    alBehaviorManagerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, 9559)
    names = alBehaviorManagerProxy.getInstalledBehaviors()
    print "Behaviours installed on the robot:"
    print names
    
    print ("\n Behaviours running on the robot")
    allItems = alBehaviorManagerProxy.getRunningBehaviors()
    for i in allItems:
        print i

def turnoff_autonomous():

    alBehaviorManagerProxy = ALProxy("ALBasicAwareness", IP_ADDRESS, 9559)
    alBehaviorManagerProxy.stopAwareness()
     
    # alBehaviorManagerProxy = ALProxy("ALAutonomousMoves", IP_ADDRESS, 9559)
    # alBehaviorManagerProxy.setExpressiveListeningEnabled(False)