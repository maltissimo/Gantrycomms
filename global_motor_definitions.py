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

"""


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

def motorNameConv(motorName):
    """
    This function converts the name of a motor to a Pmac compatible, i.e.
    Motor_i -> Motor[i]

    :param motorName:
    :return: a string with the correct motor name for interrogating PMac.
    """
    index = motorName[-1]
    convName = motorName[:len(motorName)-2] + "[" + index + "]"
    return(convName)

Motor_1_JogTa=50
Motor_1_JogTs=50
Motor_1_AbortTa=10
Motor_1_MaxSpeed=0.5
Motor_1_JogSpeed=0.5
Motor_1_HomeVel=0.5
Motor_1_PosUnit=4

Motor_2_JogTa=50
Motor_2_JogTs=50
Motor_2_AbortTa=10
Motor_2_MaxSpeed=0.5
Motor_2_JogSpeed=0.5
Motor_2_HomeVel=0.5
Motor_2_PosUnit=4

Motor_3_JogTa=50
Motor_3_JogTs=50
Motor_3_AbortTa=10
Motor_3_MaxSpeed=0.5
Motor_3_JogSpeed=0.5
Motor_3_HomeVel=0.5
Motor_3_PosUnit=4

Motor_4_JogTa=300
Motor_4_JogTs=100
Motor_4_AbortTa=-20000
Motor_4_JogSpeed=0.0049999999
Motor_4_HomeVel=0.0049999999
Motor_4_PosUnit=11

Motor_5_JogTa=100
Motor_5_JogTs=100
Motor_5_JogSpeed=10
Motor_5_PosUnit=4

Motor_6_JogTa=100
Motor_6_JogTs=100
Motor_6_AbortTa=50
Motor_6_JogSpeed=10
Motor_6_PosUnit=4
