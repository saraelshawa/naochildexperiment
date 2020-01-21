import Tkinter  as tk
from naoqi import ALProxy
from SocialPage import SocialPage
from NonSocialPage import NonSocialPage
from settings import IP_ADDRESS
from settings import PORT
import time 
import json


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, width=500, height=500)
        self.pack_propagate(False)
        
        tk.Label(self, text="Main page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        social_button = tk.Button(self, text="Social",
                  command=lambda: master.switch_frame(SocialPage))
        social_button.pack(side='left')
        social_button.config( height = 10, width = 10)
        # social_button.grid(row = 0, column =3)
        nonsocial_button = tk.Button(self, text="Non-Social",
                  command=lambda: master.switch_frame(NonSocialPage))
        nonsocial_button.pack(side='right')
        nonsocial_button.config( height = 10, width = 10)

        dance_button = tk.Button(self, text="Dance", command=self.dance)
        dance_button.pack(side='top')
        dance_button.config( height = 3, width = 10)

    def dance(self):
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
        
        time.sleep(4)
        managerProxy.stopAllBehaviors()
    

        # self.textBox = tk.Text(self, height=2, width=10)
        # self.textBox.pack()

        # tk.Button(self, text="Input file name", command=lambda: self.input_file()).pack()
    
    # def input_file(self):
    #     FILE_NAME = self.textBox.get("1.0", "end-1c")
    #     print(FILE_NAME)
    #     print("exit")
    