import Tkinter  as tk
from naoqi import ALProxy    
from sys import exit
import qi

def fun():
	tts = ALProxy("ALTextToSpeech", "169.254.124.254", 9559)
	tts.say("Hi, Sho!")
	

def quit():
    global root
    root.quit()

def eye_color():
    session = qi.Session()
    session.connect("tcp://169.254.124.254:9559")
    leds_service = session.service("ALLeds")

    # Example showing how to fade the eyes to green 
    name = 'FaceLeds'
    intensity = 0.5
    duration = 2.0
    leds_service.fadeRGB(name, "green", duration)
    leds_service.rasta(4)

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

        # if direction == "right":
        #     angleLists = [[-0.5, -0.5]]

        timeLists = [[1.0, 2.0]]
        isAbsolute  = True
        motionProxy.angleInterpolation(["HeadPitch"], angleLists, timeLists, isAbsolute)


def make_sound():
    #to do 
    tts = ALProxy("ALTextToSpeech", "169.254.124.254", 9559)
    tts.say("Ow!")


def gaze_follow():
    #to do 
    #total gaze follows: 3 right, 3 left, select randomly 
    return


root = tk.Tk()
root.geometry("500x500")
frame = tk.Frame(root)
frame.pack()



button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame, text="Hello", command=fun)
slogan.pack(side=tk.LEFT)
eye_button = tk.Button(frame, text="Eyes", fg="red", command=eye_color)
eye_button.pack(side=tk.LEFT)

sound_button = tk.Button(frame, text="Sound", fg="red", command=make_sound)
sound_button.pack(side=tk.LEFT)

gaze_following_button = tk.Button(frame, text="Gaze Follow", fg="blue", command=gaze_follow)
gaze_following_button.pack(side=tk.LEFT)


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

    # tts = ALProxy("ALTextToSpeech", "169.254.124.254", 9559)
    # tts.say("Bye, Sho!")

root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)


print("here")
root.mainloop()
