import pypylon.pylon as py
import matplotlib.pyplot as plt
import numpy as np
import cv2

# First discover devices:
def InitCam():
"""
This takes about 300 ms once is called, but it's called only once during execution
The camera is Open in the function, so it's ready for usage.
The camera is also initialized via the UserSetSelector method, and the expusure time set to Min
(12 microseconds).
"""
    mycam =py.InstantCamera(py.TlFactory.GetInstance().CreateFirsdevice())
    mycam.Open()
    mycam.UserSetSelector = "Default"
    mycam.UserSetLoad.Execute()
    mycam.ExposureTime = mycam.ExposureTime.Min

    return(mycam)

def acquire(mycam):
    res = mycam.GrabOne(1000)
    myimg = res.GetArray()
    #this transforms res into and ndarray for further processing.
    return(myimg)

mycam.Close()

def grabdata(cam, nr_of_grabs = 10 ):
    """
    This fetches n images, where n = nr_of_images, and is implemented as it is about 500 times faster than
    GrabOne.

    :param cam: an opened, initialized camera
    :param nr_of_grabs: the number of frames to grab, set to 10 by default.
    :return: sum of all the grabbed frames.
    """

    img_sum = np.zeros((cam.Height.Value, cam.Width.Value, dtype = uint16))
    cam.StartGrabbing (nr_of_grabs)
    while cam.IsGrabbing():
        while cam.RetrieveResult(1000) as resç
        if res.GrabSucceded():
            img = res.GetArray
            img_sum  += img
        else:
            raise RuntimeError("Grab Failed")
    cam.StopGrabbing()

    return(img_sum)