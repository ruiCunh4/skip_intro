# pip install opencv-python
import cv2

# pip install Pillow
from PIL import Image, ImageChops

def total_diff(cDiff):
    b, g, r = cv2.split(cDiff)
    bDiff = cv2.countNonZero(b)
    gDiff = cv2.countNonZero(g)
    rDiff = cv2.countNonZero(r)
    total = (bDiff + gDiff + rDiff)/3
    return int(total)

def auxFunc(compareSet):
    string1 = 'out1' + compareSet + '.jpg'
    string2 = 'out2' + compareSet + '.jpg'

    img1 = Image.open(string1)
    img2 = Image.open(string2)

    cImg1 = cv2.imread(string1)
    cImg2 = cv2.imread(string2)

    diff = ImageChops.difference(img1, img2)
    cDiff = cv2.subtract(cImg1, cImg2)

    # print(total_diff(cDiff))

    cv2.imwrite('outImg'+compareSet+'.jpg', cDiff)
    #if diff.getbbox():
        # print(total_diff(cDiff))
        # diff.show()

    # 621063
    # 656159
    # 696327

    # from PIL import Image
    im = Image.open('outImg'+compareSet+'.jpg').convert('L')
    pixels = im.getdata()          # get the pixels as a flattened sequence
    black_thresh = 50
    nblack = 0
    for pixel in pixels:
        if pixel < black_thresh:
            nblack += 1
    n = len(pixels)

    if (nblack / float(n)) > 0.5:
        print("Same Frame")
    else:
        print("Different Frames")

if __name__=="__main__":

    auxFunc('1')
    auxFunc('2')
    auxFunc('3')
