# importing vlc module
import vlc
  
# importing time module
import time
  
  
# creating vlc media player object
media_player = vlc.MediaPlayer()
  
# media object
media = vlc.Media("../../videos/Asobi Asobase - 10.mp4")
  
# setting media to the media player
media_player.set_media(media)
  
  
# start playing video
media_player.play()



#print(vlc.libvlc_media_player_get_length)
#print(vlc.libvlc_media_player_get_time)
#for i in range(1000):
    #vlc.libvlc_media_player_next_frame()


  
# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(4)

vTime = media_player.get_time()

print("---> vTime: " + str(vTime))

vFPS = round(media_player.get_fps())

print("---> vFPS: " + str(vFPS))

frame2time = round(((2157+10)/vFPS)*1000)

media_player.set_time(frame2time)

time.sleep(3)

# checking if it is playing
value = media_player.is_playing()
  
# printing value
print("Is playing : ")
print(value)