import math
import frame_cmp as fc
import frame_get as fg
import cv2 ##

DEFAULT_FRAME_STEP = 1000 # Frames

if __name__=="__main__":

    
    current_video = "../../videos/Asobi Asobase - 10.mp4"
    compare_video = "../../videos/Asobi Asobase - 09.mp4"

    # Check if first frame matches

    current_frame = fg.get_fst_frame(current_video)
    compare_frame = fg.get_fst_frame(compare_video)
    if (not fc.same_frame(current_frame, compare_frame)):
        print("Error: First frame does not match")
        exit(0)
    
    # Find last matching frame

    frame_index = 0
    frame_step = DEFAULT_FRAME_STEP
    while (frame_step >= 1):
        current_frame = fg.get_nth_frame_v2(current_video, frame_index)
        compare_frame = fg.get_nth_frame_v2(compare_video, frame_index)
        cv2.imwrite('../../output/Frame_' + str(frame_index) + '.jpg', current_frame) ##
        if (not fc.same_frame(current_frame, compare_frame)):
            frame_index -= frame_step
            frame_step = math.floor(frame_step/2)
            print('Step size ' + str(frame_step)) ##
        else:
            frame_index += frame_step

    # Return last matching frame

    print("Frame " + str(frame_index)) ##