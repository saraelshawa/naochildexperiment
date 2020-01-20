import Tkinter  as tk
from StartPage import StartPage
from Timer import TimerApp
from settings import IP_ADDRESS
from settings import PORT
from naoqi import ALProxy
from stand_position import stand_position

stand_position()
class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.bind('<Left>', self.leftKey)
        self.bind('<Right>', self.rightKey)
        self.bind('<Up>', self.upKey)
        self.bind('<Down>', self.downKey)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    
    def leftKey(self, event):
        print "Left key pressed"
        self.changeAngles("HeadYaw", 0.3)


    def rightKey(self, event):
        print "Right key pressed"
        self.changeAngles("HeadYaw", -0.3)

    def upKey(self, event):
        print "Up key pressed"
        # moveHead("HeadPitch", "up", 0.2, 2)
        self.changeAngles("HeadPitch", -0.15)

    def downKey(self, event):
        print "Down key pressed"
        self.changeAngles("HeadPitch", 0.15)

    def changeAngles(self, name, add_angle):
        motionProxy = ALProxy("ALMotion", IP_ADDRESS, PORT)
        useSensors    = True
        commandAngle = motionProxy.getAngles(name, useSensors)
        
        new_pos = [commandAngle[0] + add_angle]
        motionProxy.angleInterpolationWithSpeed([name], new_pos, 0.1)
        
if __name__ == "__main__":
    app = MainApp()
    app.geometry('500x500')
    app.mainloop()