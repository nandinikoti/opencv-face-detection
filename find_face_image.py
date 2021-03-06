import time
import cv2
import cv2.cv as cv
import numpy as np
from PIL import Image

"""
Find a face in an image using OpenCV.

Basic workflow:
    * Use Haar facial detection algorithm to find faces
    * Draw the picture and draw bounding boxes around faces 
"""

def main():
    
    face_settings = {
            'scaleFactor'   : 1.3,
            'minNeighbors'  : 1,
            'minSize'       : (5,5),
            'flags'         :  cv2.cv.CV_HAAR_SCALE_IMAGE|cv2.cv.CV_HAAR_DO_ROUGH_SEARCH
    }
    
    # Other flags: 
    # cv2.cv.CV_HAAR_SCALE_IMAGE
    # cv2.cv.CV_HAAR_FIND_BIGGEST_OBJECT
    # cv2.cv.CV_HAAR_DO_ROUGH_SEARCH



    ## Obama - works 
    #IMAGE_FILE                    = "images/obama.jpg"
    #face_settings['scaleFactor']  = 1.3
    #face_settings['minNeighbors'] = 1
    
    ## GWBush - works
    #IMAGE_FILE                    = "images/bush.jpg"
    #face_settings['scaleFactor']  = 1.3
    #face_settings['minNeighbors'] = 1
    
    ## Me - works 
    #IMAGE_FILE                    = "images/me.jpg"
    #face_settings['scaleFactor']  = 1.3
    #face_settings['minNeighbors'] = 1
    
    # Photo from webcam
    IMAGE_FILE                    = "images/opencv.png"
    face_settings['scaleFactor']  = 1.3
    face_settings['minNeighbors'] = 1
    
    draw_face_boxes(IMAGE_FILE, face_settings, eye_settings)



def draw_face_boxes(filename, face_settings, eye_settings):

    image = img2np_opencv(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    face_classifier0    = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    face_classifier1    = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    face_classifier2    = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

    # --------
    # FACES:

    # Get rectangle for entire face
    print("From faces:")
    rects = detect(gray, face_classifier2, face_settings)

    # Draw face rectangles
    vis = image.copy()
    draw_rects(vis, rects, (255, 0, 0))

    cv2.imwrite("images/detected_faces.jpg", vis)

    cv2.imshow('facedetect', vis)
    cv2.waitKey()



def detect(img, cascade, settings):
    """
    Given an image and a cascade object,
    detect features.
    """
    # Parameters taken verbatim from OpenCV 2.4 example:
    # https://github.com/opencv/opencv/blob/2.4/samples/python2/facedetect.py
    rects = cascade.detectMultiScale(img, 
                        **settings)

    if len(rects) == 0:
        return []

    print(rects)

    # Turn width and height of box
    # into plot-ready image coordinates.
    # rects contains (x,y),(w,h), return (x,y),(x+w,x+h)

    rects[:,2:] += rects[:,:2]
    return rects



def img2np_pillow(filename):
    """
    Load an image using Pillow 
    and convert it to a 3D Numpy array
    with shape (W, H, 3)
    """
    with Image.open(filename) as image:
        nparr = np.fromstring(image.tobytes(), dtype=np.uint8)
        nparr = im_arr.reshape((image.size[1], image.size[0], 3))
    return nparr 

def img2np_opencv(filename):
    """
    Load an image using OpenCV
    and convert it to a 3D Numpy array
    with shape (W, H, 3)
    """
    img = cv2.imread(filename)
    return img

def draw_rects(img, rects, color):
    """
    Use OpenCV to draw rectangles 
    on top of image
    """
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__=="__main__":
    main()

