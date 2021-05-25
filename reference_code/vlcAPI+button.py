import tkinter
from functools import partial

# importing vlc module
import vlc
  
# importing time module
import time


root= tkinter.Tk()


# creating vlc media player object
media_player = vlc.MediaPlayer()
# media object
media = vlc.Media("../../videos/Asobi Asobase - 10.mp4")
# setting media to the media player
media_player.set_media(media)
# start playing video
media_player.play()
time.sleep(4)
vFPS = round(media_player.get_fps())
frame2time = round(((2157+10)/vFPS)*1000)

def skip_intro(a, b):
    a.set_time(b)
    root.destroy()
    time.sleep(6)
    exit(0)

skip_action = partial(skip_intro, a=media_player, b=frame2time)
root.attributes('-topmost', 'true')
root.overrideredirect(1)
pic = tkinter.PhotoImage(file = "Button.png")
myButton = tkinter.Button(root, image = pic, command=skip_action)
root.geometry("+1100+650")
myButton.pack()

root.mainloop()
