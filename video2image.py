# pip install opencv-python
import cv2
# import logging
import os
import random
import string

def rand_string(length):
    rand_str=''.join(random.choice(
              string.ascii_lowercase
              + string.ascii_uppercase
              + string.digits)
            for i in range(length))
    return rand_str


def length_of_video(video_path):
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length


def extracting_frames(video_path, save_path,
                skip_frames = 0):
    print('*EXTRACTING PHASE*')

    _, file_name = os.path.split(video_path)

    file_name_without_ext = os.path.splitext(file_name)[0]

    length = length_of_video(video_path)
    if length == 0:
        print('Length is 0, exiting *EXTRACTING PHASE*')
        return 0
    
    cap = cv2.VideoCapture(video_path)
    count = 0 # Keep count of frames
    random_string = rand_string(5) # For naming

    # Test first frame
    ret,frame = cap.read() # ret frame returned correctly
    test_file_path = os.path.join(
                save_path,
                file_name_without_ext[:6]+ \
                '{}_{}.jpg'.format(random_string, count))

    cv2.imwrite(test_file_path, frame)
    if os.path.isfile(test_file_path):

        print('Saving Test Frame Was Sucessful,'
        +'Counting Extraction Phase')

        count = 1
        while ret and count<100*30:
            ret,frame = cap.read()
            if ret and count % skip_frames == 0:
                cv2.imwrite(os.path.join(
                        save_path,
                        file_name_without_ext[:6]+
                        '{}_{}.jpg'.format(random_string, count)),frame)
                count +=1
                print(count)
            else:
                count+=1
    else:
        print('Problem with Saving Test Frame cv2 encoding, cannot save file')
        return 0

    cap.release()
    print('*FINISHED EXTRACTION*')

if __name__=="__main__":

    public_movies = ["[mottoj] Asobi Asobase - 09 (BDRip 1920x1080 HEVC FLAC).mp4"]
    save_path = "output1"
    for movie in public_movies:
        print(movie)
        extracting_frames(movie, save_path,
                    skip_frames = 100)

    public_movies = ["[mottoj] Asobi Asobase - 10 (BDRip 1920x1080 HEVC FLAC).mp4"]
    save_path = "output2"
    for movie in public_movies:
        print(movie)
        extracting_frames(movie, save_path,
                    skip_frames = 100)