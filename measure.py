import general_comms
import global_motor_definitions
import motor_movements
import camera
import numpy as np
from datetime import datetime
import math_utils

"""
Logic: 
Get starting (i.e. zero) position
get length of measurements and/or nr of measurement steps and/or length interval/step
get nr of acquisitions per spatial points (for averaging)
get X0, Y0 of laser on CMOS
move to zero position
start measurement: 
    - acquire position from encoder ( act_pos = [gpascii.get_variable('Motor[%d].ActPos' % i, type_=float)
                                            for i in motors]
                                    home_pos = [gpascii.get_variable('Motor[%d].HomePos' % i, type_=float)
                                            for i in motors])
    Actual position must be derived as home_pos - act_pos 
    - Repeat n times:
        - acquire data from camera 
        - calculate centroid 
        - obtain Xn, Yn
        - calculate deviation as (Xn - X0) and (Yn - Y0)
        - store deviation
    - average the data
    - save encoder position, step number, data from camera. 
    - move by a step
    
Save into text: 
- generic data first: 
    - date and time of measurement start
    - date and time of measurement end 
    - X0, Y0
    - length of measurement
    - nr of step
    - length of step 
    - nr of images per measurement point (the averaging). 

- Measurement data as an array: 
    - point nr      encoder position        abs position       centroid position

"""

def mytime():
    """

    :return: dd/mm/yyy HH:MM:SS
    """
    now = datetime.now()
    d1 =  now.strftime("%d/%m/%Y %H:%M:%S")
    return(d1)

length = 100 # length of measurement in mm
nr_points = 50 # nr of points per measurement along the mirror
sampling_step =  length/nr_points # measurement step size, i.e. sampling of mirror
av_pts = 2
default_meas_data =(length, nr_points,sampling_step , av_pts)

def set_start_pos(shell):
    print("The measurement needs a starting position, please place the head at the desired one, type done when finished")
    if (str(input)=="done"):
        start_pos = global_motor_definitions.getMotorPos(shell)
    else:
        print("Run set_Start_pos again")
        return("No_start_Pos")
    return(start_pos)

def goto_start(shell, start_pos):
    start_pos = set_Start_pos(shell)
    move = global_motor_definition.move(shell, axis = "X", speed = "linear", mode = "abs", length = start_pos)
    return()

def set_meas_data():
    print("Please input the length of the measurement, in mm: ")
    length = float(input())
    print("Please enter the number of average images per acquisition point: ")
    av_pts = int(input())
    print("Would you like to specify your measurement by nr of points (p) or sampling step (s)?")
    choice = str(input())
    if choice == "p":
        print("please enter the number of points for your measurement: ")
        nr_points = int(input())
        meas_data = [length, nr_points, length/nr_points, av_pts, choice]
        return (meas_data)

    elif choice == "s":
        print("Please enter the sampling step of your measurement, in mm: ")
        sampling_step = float(input())
        return([length, length/sampling_step, sampling_step, av_pts, choice])

    else:
        return default_meas_data

my_cam = camera.InitCam()

meas_data = set_meas_data() # this specifies length, nr of points, sampling step and averaging images per point.


def nodeflection(cam):
    """
    this is to output the ZERO deflection centroid.
    :param cam: an open camera
    :return: the centroid of the undeflected laser beam.
    """
    img = camera.grabdata(cam, 20)
    return math_utils.get_centroid(img)

zero_defl = [0,0] #this is useful for measurments purposes

#data_point = math_utils.deviation(zero_defl, data)
def measure(cam,shell,start_pos, meas_data):
    start = mytime()
    output = start
    if zero_defl == [0,0]:
        zero_defl = nodeflection(my_cam)

    goto_start(shell, start_pos) #moves X stage to start position
    centroid = np.zeros(meas_data[3], 2)

    for i in range (meas_data[1]):
        data = math_utils.get_centroid((camera.grabdata(cam, meas_data[3])) /meas_data[3])
        data_point = math_utils.deviation(zero_defl, data)
        output += str (data_point) + "\n"
        motor_movements.left(shell, meas_data[2])

    end = mytime()
    output += end
    np.savetxt(output)

    return("Measurement done!")













