import Tkinter  as tk
# from StartPage import StartPage


class SocialPage(tk.Frame):
    def x(self):
        return

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='lightblue')
        tk.Label(self, text="Social Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Make Sound", command=self.x()).pack()
        tk.Button(self, text="React to Movement", command=self.x()).pack()
        tk.Button(self, text="Wave hand", command=None).pack()

    