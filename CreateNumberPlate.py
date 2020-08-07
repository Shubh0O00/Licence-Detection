import cv2
import os
import GetPlateBox
import numpy as np

def CropImage(img,tl,br): # Returns cropped image after taking required address and image
    crop_img = img[tl[1]:br[1],tl[0]:br[0]]
    return crop_img

def CreatePlates(folder): # folder is where input images are stored
    file_count = os.listdir(folder)
    n = len(file_count)
    # Get images one by one and create numberplate images:
    for i in range(1,n+1):
        s= folder+'/'+str(i)+'.jpg'
        frame = cv2.imread(s)                  
        results = GetPlateBox.Detect(frame) # Returns list containing number plate information
        for result in results:
            tl = GetPlateBox.tl_box_coord(result)
            br = GetPlateBox.br_box_coord(result)
            crop_img = CropImage(frame,tl,br)
            filename = 'Identified_License_Plate_Images/plate'+str(i)+'.jpg'
            cv2.imwrite(filename,crop_img)

