import DarkflowNet
import numpy as np

net = DarkflowNet.NetConfig('bin/yolov2-tiny_6000_numplate.weights','cfg/yolov2-tiny_numplate.cfg',0.4)
def Detect(img):
    results = net.return_predict(img) # Returns list containing number plate information
    return results

def tl_box_coord(result): # Returns top left pixel values for given image
    return (result['topleft']['x'], result['topleft']['y'])

def br_box_coord(result): # Returns bottom right pixel values for given image
    return (result['bottomright']['x'], result['bottomright']['y'])


