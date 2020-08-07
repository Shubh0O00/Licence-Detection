import cv2
from darkflow.net.build import TFNet
import numpy as np
import os
#import mainOCR.py

def net_config(weights,cfg_file,threshold): # Configuration function to intiate darkflow network for our model
    options = {
    'model': cfg_file,
    'load': weights,
    'threshold': threshold,
    }
    tfnet = TFNet(options)                 # Initiating neural network
    return tfnet

def tl_box_coord(result): # Returns top left pixel values for given image
    return (result['topleft']['x'], result['topleft']['y'])

def br_box_coord(result): # Returns bottom right pixel values for given image
    return (result['bottomright']['x'], result['bottomright']['y'])

# Create neural net:
net = net_config('bin/yolov2-tiny_6000_numplate.weights','cfg/yolov2-tiny_numplate.cfg',0.4)

def CropImage(img,tl,br): # Returns cropped image after taking required address and image
    crop_img = img[tl[1]:br[1],tl[0]:br[0]]
    return crop_img

def CreatePlates(folder): # folder is where input images are stored
    file_count = os.listdir(folder)
    n = len(file_count)
    # Get images one by one and create numberplate images:
    for i in range(1,n+1):
        s= 'Input_Images/'+str(i)+'.jpg'
        frame = cv2.imread(s)                  
        results = net.return_predict(frame) # Returns list containing number plate information
        for result in results:
            tl = tl_box_coord(result)
            br = br_box_coord(result)
            crop_img = CropImage(frame,tl,br)
            filename = 'Identified_License_Plate_Images/plate'+str(i)+'.jpg'
            cv2.imwrite(filename,crop_img)

def main():
    print('welcome!')
    CreatePlates('Input_Images')

if __name__ == "__main__":
    main()

    