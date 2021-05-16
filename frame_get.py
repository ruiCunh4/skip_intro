import cv2



# Returns nth frame of a video

def get_nth_frame(video, n):
    
    capture = cv2.VideoCapture(video)

    frame_index = 0
    has_frame,frame = capture.read()
    while has_frame:
        if frame_index == n:
            capture.release()
            return frame
        else:
            has_frame,frame = capture.read()
            frame_index += 1

    capture.release()
    print('Error: End of video')
    exit(0)



# Returns first frame of a video

def get_fst_frame(video):
    return get_nth_frame(video, 0)