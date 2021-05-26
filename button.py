from functools import partial
import tkinter as tk
import time ##

BUTTON_POSITION = "+1100+650"



# Skips to a given time

def skip_action(root, mp, t):
    mp.set_time(t)
    root.destroy()
    time.sleep(5) ##



# Creates a Skip Intro button

def create(time, media_player):

    root= tk.Tk()
    skip_intro = partial(skip_action, root=root, mp=media_player, t=time)
    root.attributes('-topmost', 'true')
    root.overrideredirect(1)
    button_img = tk.PhotoImage(file = "Button.png")
    myButton = tk.Button(root, image = button_img, command=skip_intro)
    root.geometry(BUTTON_POSITION)
    myButton.pack()
    root.mainloop()