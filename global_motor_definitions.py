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
    :return: 5,6, Z, A, B, C depending on the user choice
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
    The system of reference is inferred from the motor called.

    :param shell: required, a SSH shell for comms.
    :param axis: axis for motion
    :param speed: interpolated (i.e. slow, pmac default) or rapid.
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
"""
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
"""