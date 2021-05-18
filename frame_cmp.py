import cv2

BLACK_TRESHOLD = 50 # Brightness
SAME_FRAME_TOLERANCE = 0.99 # Similarity Percentage



# Determins if to frames are the same

def same_frame(frame_1, frame_2):

    pixel_count = 0
    black_pixel_count = 0

    frame_subtract = cv2.subtract(frame_1, frame_2)
    for row in frame_subtract:
        for pixel in row:
            b,g,r = pixel
            brightness = int(r) + int(g) + int(b)
            pixel_count += 1
            if (brightness < BLACK_TRESHOLD):
                black_pixel_count += 1
    
    if (float(black_pixel_count/pixel_count) > SAME_FRAME_TOLERANCE):
        print('Same frame') ##
        return True
    else:
        print('Different frames') ##
        return False
