import Tkinter  as tk


class GazeFollowPage(tk.Frame):
    def x(self):
        return

    def __init__(self, master, **kw):
        frame_1 = tk.Frame.__init__(self, master, **kw)
        tk.Frame.configure(self,bg='lightblue')
        tk.Label(self, text="Gaze Follow Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

    