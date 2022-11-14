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
from general_comms import *
def axis_conversion(axis):
    """
    Converts axis as input by user back into Pmac-understandable format

    :param axis: X, Y, Z, pitch, roll, rot
    :return: X,Y, Z, A, B, C depending on the user choice
    """
    if axis == "X" or axis == "x":
        ret = "X"
    elif axis == "Y" or axis == "y":
        ret = "Y"
    elif axis == "Z" or axis == "z":
        ret = "Z"
    elif axis == "PITCH" or axis == "Pitch" or axis =="pitch":
        ret = "B"
    elif axis == "ROLL" or axis == "Roll" or axis == "roll":
        ret = "A"
    elif axis == "ROT" or axis == "Rot" or axis == "rot" or axis == "Rotation" or axis == "rotation" or axis == "YAW" or axis == "Yaw" or axis == "yaw":
        ret = "C"

    return(ret)

def home_all(pmac_conn):
    """
    This function homes all axes as per QSys protocol. It should be run only once the system is turned on.
    :return:
    """
    axes = "selectAxes = selectAll\n"
    pmac_conn.send(axes)
    home = "requestHost = requestHome\n"
    pmac_conn.send(home)
    return ()

def Idle(shell):
    """
    This funcion performs a requestIdle command as per Qsys protocols.
    :param shell:  a paramiko shell connected to pmac
    :return:
    """
    axes = "selectAxes = selectAll\n"
    shell.send(axes)
    idle = "requestHost = requestIdle\n"
    shell.send(idle)
    return("Idling all axes")

def move(shell, axis, speed, mode, length):
    """
    See motor definition above!!!
    The system of reference is inferred from the motor called. This is a general move, not a specific one

    :param shell: required, a SSH shell for comms.
    :param axis: axis for motion
    :param speed: linear (i.e. slow, pmac default) or rapid.
    :param mode: absolute (abs) or relative (inc)
    :param length: length of motion
    :return: a string containing the move, to be passed to a shell.
    """
    if axis == "X" or axis == "Y":
        SR = str(3)
    elif  axis == "Pitch" or axis == "pitch" or axis == "Roll" or axis == "roll" or axis == "Z":
        SR = str(1)
    elif axis == "Rot" or axis == "rot" or axis == "rotation" or axis == "Rotation":
        SR = str(2)

    if mode == "relative" or mode == "Rel" or mode == "Relative":
        mode == "inc"

    else:
        mode == "abs"

    command = str( "&" + SR + " cpx " + speed + " " + mode + " " + axis_conversion(axis) + str(length) + "\n")
    shell.send(command)
    output = str("Move: " + command + " sent as requested")

    return (output)


def motorNameConv(motorName):
    """
    This function converts the name of a motor to a Pmac compatible, i.e.
    Motor_i -> Motor[i]

    :param motorName:
    :return: a string
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