import general_comms
import global_motor_definitions
import motor_movements

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

length = 100 # length of measurement in mm
nr_points = 50 # nr of points per measurement
sampling_step =  length/nr_points # measurement step size, i.e. sampling of mirror
av_pts = 2
default_meas_data =(length, nr_points,sampling_step , av_pts)

def set_Start_pos(shell):
    print("The measurement needs a starting position, please place the head at the desired one, type done when finished")
    if (str(input)=="done"):
        start_pos = global_motor_definitions.getMotorPos(shell)
    else:
        print("Run set_Start_pos again")
        return("No_start_Pos")
    return(start_pos)

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
        return([length, length/sampling_step, samppling_step, av_pts, choice])

    else:
        return(default_meas_data)

# TODO: implement measurement routine on the basis of what is written here above

def measurement():








