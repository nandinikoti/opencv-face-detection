# OpenCV Face Detection

This repository contains utility scripts for doing facial detection in images using OpenCV.

Most of these scripts are experiments. The goal is to incorporate these scripts
into scripts for a Raspberry Pi facial detection device - see the [pi-opencv](https://github.com/charlesreid1-raspberry-pi/pi-opencv) 
repository.

## Repository Organization

Completed tasks:
* <s>Take a photo using a webcam</s>
* <s>Basic face-finding code</s>
* <s>Consistent face-finding across multiple test photographs</s>

In-progress tasks:
* Webcam face-finding script
* Find eyes in a photograph (using test images from internet)
* Find eyes in a webcam photograph (using webcam photos)
* Find a face that may be rotated up to N degrees (using webcam)
* Detect sideways faces using eyes angle

## Take a Photo Using Webcam

`take_photo.py` - takes a photo with a webcam

* Imports OpenCV
* Captures an image from the specified camera device
* Transposes the image (rotate right)
* Saves the images to a file
* Uses imshow to show the images on screen
* (Future work) image is a numpy array, so do further processing/exports

<img src="images/pi-opencv.jpg" width="200px" />

## Basic Facial Recognition

`basic_face_detection.py` - illustrate basic face detection

* Illustrates facial detection in the simplest script possible
* Cascade classifier is sensitive to parameter choices
* Does not generalize well

**Expected output:**

<img src="images/output_basic_face_detection.jpg" width="300px"/>

## Consistently Find a Face

**STATUS: DONE**

`find_face_image.py` - more generalized face detection script

* Open an image on disk using OpenCV or Pillow
* Create cascade classifier to find faces
* Get rectangles containing faces
* Draw rectangles around faces
* Get rectangles containing eyes
* Draw rectangles around eyes
* Show the image of the face with rectangles

This script worked on multiple face photos, including two
from the webcam that will be used with the final Raspberry Pi 
setup (one low-res, one high-res).

## Find Face in Webcam Photograph

`webcam_face.py`

* Stream images from a webcam continuously
* Search for faces
* If faces are detected, output detected faces and bounding boxes to image
* Monitor output with a barebones web server

## Find Rotated Faces

Notes:
* https://stackoverflow.com/questions/5015124/rotated-face-detection#15997139

## Detect 



## Notes

Notes:
* It's easy to write a script that *usually* detects faces, or detects *one* eye, but 
    getting the task to work consistently, and always find a face and two eyes, is a pain.
* The process is extremely sensitive to the parameters used for the cascading classifier.
    Each different photo of a face requires different `scaleFactor` and `minNeighbors` settings
* Eyes are also difficult to detect without fiddling with settings that are specific to each image.
* [This](https://stackoverflow.com/questions/16128637/opencv-haarlike-eye-detection#16131846) SO question mentions an eye pair Haar cascade file.
* [opencv-contrib](https://github.com/opencv/opencv_contrib) repo has additional cascade .xml files
* See [opencv-contrib modules/face/data/cascades](https://github.com/opencv/opencv_contrib/tree/master/modules/face/data/cascades)


