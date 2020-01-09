import Tkinter  as tk
from naoqi import ALProxy
from SocialPage import SocialPage
from NonSocialPage import NonSocialPage
from settings import IP_ADDRESS
from settings import PORT
import time 

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Main page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Social",
                  command=lambda: master.switch_frame(SocialPage)).pack()
        tk.Button(self, text="Non-Social",
                  command=lambda: master.switch_frame(NonSocialPage)).pack()
        tk.Button(self, text="Dance", command=self.dance).pack()
    
    def dance(self):

        # aup = ALProxy("ALAudioPlayer", IP_ADDRESS, PORT)
        # aup.playFile("/naoqi/nao_japanese_song.wav")
        # fileId = aup.post.playFile("/home/sara/repos/naochildexperiment/nao_japanese_song.mp3")
        # aup.play(fileId)
        # ap.loadSoundSet("Aldebaran")
        # fileId = ap.post.playSoundSetFile("filename")

        managerProxy = ALProxy("ALBehaviorManager", IP_ADDRESS, PORT)
        managerProxy.startBehavior('untitled-690f7b/japanese_song')

        managerProxy.runBehavior('animations/Stand/Gestures/Thinking_4')

        managerProxy.runBehavior("animations/Stand/Gestures/You_2")

        managerProxy.runBehavior("animations/Stand/Gestures/Wings_2")
        managerProxy.runBehavior('animations/Stand/Gestures/ShowSky_4')
        managerProxy.runBehavior('animations/Stand/Gestures/Kisses_1')
        managerProxy.runBehavior('animations/Stand/Waiting/LoveYou_1')
        managerProxy.runBehavior("animations/Stand/Waiting/HideEyes_1")
       
        managerProxy.runBehavior("animations/Stand/Gestures/Wings_2")
        managerProxy.runBehavior('animations/Stand/Gestures/ShowSky_4')
        
        

        
        # time.sleep()
        managerProxy.stopAllBehaviors()
        # aup = ALProxy("ALAudioPlayer", IP_ADDRESS, PORT)
        # fileId = aup.loadFile("/home/sara/repos/naochildexperiment/nao_japanese_song.mp3")
        # aup.play(fileId)