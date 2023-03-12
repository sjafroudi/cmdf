from flask import Flask, render_template
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
import cohere  
from cohere.classify import Example

coh = cohere.Client(...)

app = Flask(__name__)

@app.route("/")

def find_color(filename):
    # open the image using the PIL library
    img = Image.open(filename)
    # get the colors in the image, sorted by count
    colors = img.getcolors(img.size[0] * img.size[1])
    sorted_colors = sorted(colors, reverse=True, key=lambda x: x[0])
    # the dominant color is the color with the highest count
    dominant_color = sorted_colors[0][1]
    # return the dominant color as a tuple of RGB values
    return dominant_color

def hello_world():
    path = '/Users/sara/cmdf/backend/images/palette.png'
    img = cv2.imread(path)
    copy = '/Users/sara/cmdf/backend/images/copyImage.png'
    cv2.imwrite(copy, img)
    # convert BGR to RGB to be suitable for showing using matplotlib library
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # make a copy of the original image
    cimg = img.copy()
    # convert image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply a blur using the median filter
    img = cv2.medianBlur(img, 5)
    # finds the circles in the grayscale image using the Hough transform
    circles = cv2.HoughCircles(image=img, method=cv2.HOUGH_GRADIENT, dp=0.9, 
                                minDist=80, param1=110, param2=39, maxRadius=70)
    img = cv2.imread(path)
    temp_image = np.zeros_like(img)
    for co, i in enumerate(circles[0, :], start=1):
        # print("co: " + str(co) + " i: " + str(i))
        # draw the outer circle
       # cv2.circle(cimg,(int(i[0]),int(i[1])),int(i[2]),(0,255,0),2)
        # draw the center of the circle
       # cv2.circle(cimg,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),3)
        # add text to the center of the circle
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(co)  # number of the circle
        text_size = cv2.getTextSize(text, font, 1, 2)[0]
        text_x = int(i[0] - text_size[0]/2)
        text_y = int(i[1] + text_size[1]/2)
        # cv2.putText(img, text, (text_x, text_y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        # draw a circle on the temporary image with the same center and radius as the current detected circle
        cv2.circle(temp_image, (int(i[0]), int(i[1])), int(i[2]), (255, 255, 255), -1)
        
        x = int(i[0] - i[2])
        y = int(i[1] - i[2])
        w = h = int(i[2] * 2)
        # crop the original image using the ROI (region of interest)
        cropped_img = cimg[y:y+h, x:x+w]
        # get the dimensions of the input image
        h, w = cropped_img.shape[:2]
        # calculate the dimensions of the cropped image
        crop_w = int(w * 0.65)
        crop_h = int(h * 0.65)
        # calculate the starting coordinates of the cropped image
        start_x = int((w - crop_w) / 2)
        start_y = int((h - crop_h) / 2)
        # extract the center region of the image with the cropped dimensions
        cropped_img = cropped_img[start_y:start_y+crop_h, start_x:start_x+crop_w]
        # crop image as a circle
        filename = '/Users/sara/cmdf/backend/images/croppedImage' + str(co) + '.png'
        color = find_color(filename)
        inputs=['Describe this color in 2 words or less: ',
            str(color)
            ]
        examples=[
            Example("Describe this color in 2 words or less: (129, 132, 198)", "Muted Lavender"),
            Example("Describe this color in 2 words or less: (74, 115, 209)", "Bright Blue"),
            Example("Describe this color in 2 words or less: (175, 160, 76)", "Mustard Yellow"),
            Example("Describe this color in 2 words or less: (69, 151, 231)", "Sky Blue")
            ]
        img_description = coh.classify(
            inputs=inputs,
            examples=examples,
            )
        print(color)
        cv2.putText(img, img_description, (text_x, text_y), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imwrite(filename, cropped_img)
        
    # print the number of circles detected
    print("Number of circles detected:", co)
    # Filename
    filename = '/Users/sara/cmdf/backend/images/savedImage.png'
    cv2.imwrite(filename, img)
    return "hi"

hello_world()