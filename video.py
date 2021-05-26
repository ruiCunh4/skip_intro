import vlc



# Starts video

def play(media_player):
    media_player.play()



# Calculates the timestamp of a given frame index

def frame_timestamp(frame_index, media_player):
    fps = round(media_player.get_fps())
    return round( ( (frame_index+10)/fps )*1000 )