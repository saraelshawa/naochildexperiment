import Tkinter  as tk
from naoqi import ALProxy    
from sys import exit
import qi
import time
from GazeFollowInteraction import GazeFollowInteraction
from hand_wave import hand_wave
from gangam_style import gangam_style_position, gangam_style_dance
from stand_position import stand_position

# def fun():
	# tts = ALProxy("ALTextToSpeech", "169.254.124.254", 9559)
	# tts.say("Hi, Sho!")
	
IP_ADDRESS = "169.254.186.86"
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
    intensity = 0.5
    duration = 2.0
    leds_service.fadeRGB(name, "green", duration)
    leds_service.rasta(1)


def moveHead(type, direction):
    motionProxy = ALProxy("ALMotion", "169.254.124.254", 9559)

    #left or right
    if type == "HeadYaw":
        if direction == "left":
            angleLists = [[0.5, 0.5]]
        if direction == "right":
            angleLists = [[-0.5, -0.5]]

        timeLists = [[1.0, 2.0]]
        isAbsolute  = True
        motionProxy.angleInterpolation(["HeadYaw"], angleLists, timeLists, isAbsolute)
    #up or down 
    if type == "HeadPitch":
        if direction == "up":
            angleLists = [[-0.2, -0.2]]
        if direction == "down":
            angleLists = [[0.5, 0.5]]
            
        timeLists = [[1.0, 2.0]]
        isAbsolute  = True
        motionProxy.angleInterpolation(["HeadPitch"], angleLists, timeLists, isAbsolute)


def make_sound():
    #to do 
    stand_position()
    tts = ALProxy("ALTextToSpeech", IP_ADDRESS, 9559)
    tts.say("Ow!")



gazeFollowInteration = GazeFollowInteraction()
def gaze_follow():
    next_move = gazeFollowInteration.get_next_move()
    if next_move == GazeFollowInteraction.LEFT_HEAD_MOVE:
        moveHead("HeadYaw", "left")
    elif next_move == GazeFollowInteraction.RIGHT_HEAD_MOVE:
        moveHead("HeadYaw", "right")
    return


def dance():
    stand_position()
    managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, 9559)
    managerProxy.runBehavior("gangnamstyle1234-91e48b/GangnamStyle")


    # aup = ALProxy("ALAudioPlayer", "169.254.124.254", 9559)
    # fileId = aup.loadFile("/home/sara/repos/testing_nao/file_example_WAV_1MG.wav")
    # time.sleep(5)
    # aup.play(fileId)

def hand_wave_func():
    stand_position()
    hand_wave()
    # tts = ALProxy("ALAnimationPlayer", IP_ADDRESS, 9559)
    # tts.run("animations/Stand/Gestures/Hey_1!")

root = tk.Tk()
root.geometry("500x500")
frame = tk.Frame(root)
frame.pack()
root.protocol('WM_DELETE_WINDOW', root.quit())



button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)
# slogan = tk.Button(frame, text="Hello", command=fun)
# slogan.pack(side=tk.LEFT)
eye_button = tk.Button(frame, text="Eyes", fg="red", command=eye_color)
eye_button.pack(side=tk.LEFT)

sound_button = tk.Button(frame, text="Sound", fg="red", command=make_sound)
sound_button.pack(side=tk.LEFT)

gaze_following_button = tk.Button(frame, text="Gaze Follow", fg="blue", command=gaze_follow)
gaze_following_button.pack(side=tk.LEFT)

play_dance_button = tk.Button(frame, text="Dance", fg="blue", command=dance)
play_dance_button.pack(side=tk.LEFT)

wave_hand_button = tk.Button(frame, text="Wave hand", fg="blue", command=hand_wave_func)
wave_hand_button.pack(side=tk.LEFT)


def leftKey(event):
    print "Left key pressed"
    moveHead("HeadYaw", "left")

def rightKey(event):
    print "Right key pressed"
    moveHead("HeadYaw", "right")

def upKey(event):
    print "Up key pressed"
    moveHead("HeadPitch", "up")

def downKey(event):
    print "Down key pressed"
    moveHead("HeadPitch", "down")

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