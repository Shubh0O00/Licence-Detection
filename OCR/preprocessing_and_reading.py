import cv2                  
import pytesseract          #For identifiying text in images
import numpy as np
 
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR\\tesseract.exe'


#Function to take the address of an image
#And return a list containing top possible output for image to text conversion
#Addr is an input of type string

def change_the_image(addr):

    img = cv2.imread(addr,0)    

    #Copying the image into another variable and adding a white background to it to show output
    img1 = img
    img1 = cv2.copyMakeBorder(img1, 300, 300, 600, 600, cv2.BORDER_CONSTANT,value=255)

    l=list()

    #Nested loop to vary the iteration value for images from 0 to 2 to obtain a clearer image
    for i in range(0,2):
        img = cv2.imread(addr,0)
        img=cv2.morphologyEx(img,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=i)
        for j in range(0,2):
            img=cv2.morphologyEx(img,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=j)
            img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
            custom_config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(img, config=custom_config)
            l.append(text)
            print("Plate no==>")
            print(text)
            print("Ended")
    
    return l,img1
