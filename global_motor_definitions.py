"""
These are some global definitions that may be useful during measurements. The values are taken 
directly from the config file of the Gantry PMac. It can be found inside the 
390-main/code/10420-01/LTP-RTT/LTP-RTT/Configuration 
folder

The units of measurements (PosUnits) are as follows (taken from the PowerBrik LV Arm User Manual, page 150>

Motor[x].PosUnit            Unit Name
0                        m.u.       (motor unit)
1                            Count      (ct)
2                            Meter      (m)
3                         Millimiter    (mm)
4                         Micrometer    (µm)
5                         Nanometer     (nm)
6                         Picometer     (pm)
7                              Inch     (in)                           
8                           mil         (in/1000)
9                           Revolution
10                          Radian      (rad)
11                          Degree      (deg)
12                          Gradian     (grad)
13                          Arcminute   (')
14                          Arcsecond   ('')

Further to this, here below the motor definitions: 

// [MOTOR_DEF]
&0#0->0
&1#1->i
#2->i
#3->i
&2#4->c
&3#5->x
#6->y
&0#7->0
#8->0
#9->0
#10->0
#11->0
#12->0

Author M. Altissimo c/o Elettra Sincrotrone Trieste SCpA

""""

def axis_conversion(axis):
    """
    Converts axis as input by user back into Pmac-understandable format

    :param axis: X, Y, Z, pitch, roll, rot
    :return: 5,6, Z, A, B, C depending on the user choice
    """
    if axis == "X" or axis == "x":
        ret = "5"
    elif axis == "Y" or axis == "y":
        ret = "6"
    elif axis == "Z" or axis == "z":
        ret = "Z"
    elif axis == "PITCH" or axis == "Pitch" or axis =="pitch":
        ret = "B"
    elif axis == "ROLL" or axis == "Roll" or axis == "roll":
        ret = "A"
    elif axis == "ROT" or axis == "Rot" or axis == "rot" or axis == "Rotation" or axis == "rotation" or axis == "YAW" or axis == "Yaw" or axis == "yaw":
        ret = "C"

    return(ret)
    

Motor[1]_JogTa=50
Motor[1]_JogTs=50
Motor[1]_AbortTa=10
Motor[1]_MaxSpeed=0.5
Motor[1]_JogSpeed=0.5
Motor[1]_HomeVel=0.5
Motor[1]_PosUnit=4

Motor[2]_JogTa=50
Motor[2]_JogTs=50
Motor[2]_AbortTa=10
Motor[2]_MaxSpeed=0.5
Motor[2]_JogSpeed=0.5
Motor[2]_HomeVel=0.5
Motor[2]_PosUnit=4

Motor[3]_JogTa=50
Motor[3]_JogTs=50
Motor[3]_AbortTa=10
Motor[3]_MaxSpeed=0.5
Motor[3]_JogSpeed=0.5
Motor[3]_HomeVel=0.5
Motor[3]_PosUnit=4

Motor[4]_JogTa=300
Motor[4]_JogTs=100
Motor[4]_AbortTa=-20000
Motor[4]_JogSpeed=0.0049999999
Motor[4]_HomeVel=0.0049999999
Motor[4]_PosUnit=11

Motor[5]_JogTa=100
Motor[5]_JogTs=100
Motor[5]_JogSpeed=10
Motor[5]_PosUnit=4

Motor[6]_JogTa=100
Motor[6]_JogTs=100
Motor[6]_AbortTa=50
Motor[6]_JogSpeed=10
Motor[6]_PosUnit=4
M