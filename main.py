import subprocess

#to activate the virtual environment
cmd = subprocess.Popen('Scripts\\activate',shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
output_byte = cmd.stdout.read() + cmd.stderr.read()


from OCR import preprocessing_and_reading
from OCR import list_modification
import cv2
import os

from OCR import output_text_file
from datetime import datetime
import CreateNumberPlate



#to run number plate detection
CreateNumberPlate.CreatePlates('Input_Images')

#to run the OCR part
file_count = os.listdir('Identified_License_Plate_Images/')
n = len(file_count)

for i in range(1,n+1):
    addrr = 'Identified_License_Plate_Images/plate'+str(i)+'.jpg'
    list1,img1 = preprocessing_and_reading.change_the_image(addrr)
    main_list = list_modification.list_cleaner(list1)
    print("####################")
    print("The list is:")
    print(main_list) 
    print("####################")
    s_to_put = 'Top choices: ' + str(main_list)
    output_text_file.string_insert('plate'+str(i), s_to_put)
    img1 = cv2.putText(img1,s_to_put,(100,90),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA,False)
    filename = 'Output/plate'+str(i)+'.jpg'
    cv2.imwrite(filename, img1)
    cv2.imshow('img1', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
