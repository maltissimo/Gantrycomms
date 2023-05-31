import pypylon.pylon as py
import matplotlib.pyplot as plt
import numpy as np
import cv2

# First discover devices:
def InitCam():

    tlf = py.TlFactory.GetInstance()
    devices = tlf.EnumerateDevices()

    mycam = py.InstantCamera(tlf.CreateDevice(devices[0]))

    # if there is only device:
    mycam = py.InstantCamera(tlf.CreateFirstDevice())

    return(mycam)

mycam.Open()

"""
MUST select PixelFormat as follows: 
mycam.PixelFormat.Symbolics

this will output a numenr of possibilities,and you'll have to choose what suits best. 
It should be a greyscale of some sort, in order for the array to be understandable. 
Once that is done: 
mycam.PixelFormat = ONE OF THE RESULTS JUST OBTAINED.

"""


def acquire(mycam):
    res = mycam.GrabOne(1000)
    myimg = res.GetArray()
    #this transforms res into and ndarray for further processing.
    return(myimg)

mycam.Close()

def 