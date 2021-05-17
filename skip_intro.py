import math
import frame_cmp as fc
import frame_get as fg
import cv2 ##

DEFAULT_FRAME_STEP = 1000 # Frames

if __name__=="__main__":

    
    current_video = "../../videos/Asobi Asobase - 09.mp4"
    compare_video = "../../videos/Asobi Asobase - 10.mp4"

    # Check if first frame matches

    current_frame = fg.get_fst_frame(current_video)
    compare_frame = fg.get_fst_frame(compare_video)
    cv2.imwrite('../../output/current_frame.jpg',current_frame) ##
    if (not fc.same_frame(current_frame, compare_frame)):
        print("Error: First frame does not match")
        exit(0)
    
    # Find last matching frame

    frame_index = 0
    frame_step = DEFAULT_FRAME_STEP
    while (frame_step >= 1):
        current_frame = fg.get_nth_frame(current_video, frame_index)
        compare_frame = fg.get_nth_frame(compare_video, frame_index)
        if (not fc.same_frame(current_frame, compare_frame)):
            frame_index -= frame_step
            frame_step = math.floor(frame_step/2)
            print('New step size ' + frame_step) ##
            # Error: can only concatenate str (not "int") to str ##
        else:
            frame_index += frame_step

    # Return last matching frame

    print("Frame " + frame_index) ##
    # Error: can only concatenate str (not "int") to str ##
    last_matching_frame = fg.get_nth_frame(current_video, frame_index) ##
    cv2.imwrite('../../output/last_matching_frame.jpg',last_matching_frame) ##
    first_mismatching_frame = fg.get_nth_frame(current_video, frame_index + 1) ##
    cv2.imwrite('../../output/first_mismatching_frame.jpg',first_mismatching_frame) ##