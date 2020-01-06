import Tkinter  as tk

from SocialPage import SocialPage
from NonSocialPage import NonSocialPage

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Main page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Social",
                  command=lambda: master.switch_frame(SocialPage)).pack()
        tk.Button(self, text="Non-Social",
                  command=lambda: master.switch_frame(NonSocialPage)).pack()