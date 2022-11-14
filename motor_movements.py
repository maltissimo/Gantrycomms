"""
This set of functions is written to make the movements more akin to natural language.
See the definitions of motors in:
global_motor_definitions.py

and the help in
help_functions.py

in particular, from  help_reference():

 X = 5,    Coordinate System:  3, units: microns
 Y = 6,    Coordinate system: 3 units: microns
 Z = Z,    Coordinate system: 1, moves the RTT stage up and down, units: microns
 Roll = A,  Coordinate System: 1, tips the RTT stage towards front or back, i.e. rotation around X axis, units: degrees
 Pitch = B, Coordinate System: 1, tilts the RTT stage towards left and right, Rotation around Y axis, units: degrees
 Rot = C,   Coordinate System: 2, rotation around Z axis, units: degrees

All motions are in linear mode, i.e. slow, by default, unless specified explicitly by the function call.

Author M. Altissimo c/o Elettra Sincrotrone Trieste SCpA

"""
(shell, axis, speed, mode, length)


"""
relative motions
"""
#X axis, CS 3, units: microns
def left (shell, speed = "linear", length):
    """
    Moves the X head carriage to the left, i.e. positive relative motion.

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length: length of motion in microns
    :return:
    """
    move = "&3 cpx " + speed + "X" + str(length) +"\n"
    shell.send(move)
    return()

def right(shell, speed = "linear", length):
    """
    Moves the X head carriage to the right, i.e. negative relative motion
    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length: length of motion in microns. The function makes it negative.
    :return:
    """
    move = "&3 cpx " + speed + "X" + str(-length) + "\n"
    shell.send(move)
    return()

#Y axis, CS 3, units:microns

def forward (shell, speed = "linear", length):
    """
    Moves the RTT stage foward, i.e. positive relative motion

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length:  length of motion in microns.
    :return:
    """
    move = "&3 cpx " + speed + "Y" + str(length) + "\n"
    shell.send(move)
    return ()

def back (shell, speed = "linear", length):
    """
    Moves the RTT stage bac, i.e. negative relative motion

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length: length of motion in microns. The function makes it negative
    :return:
    """
    move = "&3 cpx " + speed + "Y" + str(-length) + "\n"
    shell.send(move)
    return ()

#Z axis, CS 2, units: microns
def up (shell, speed = "linear", length):
    """
    Moves the RTT stage up, i.e. relative positive motion

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length: length of motion in microns.
    :return:
    """
    move = "&2 cpx " + speed + "Z" + str(length) + "\n"
    shell.send(move)
    return()

def down (shell, speed = "linear", length):
    """
    Moves the RTT stage down, i.e. relative positive motion

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length: length of motion in microns. The function makes it negative
    :return:
    """

    move = "&2 cpx " + speed + "Z" + str(-length) + "\n"
    shell.send(move)
    return()

#Rotation axis, CS 2, units: degrees

def rot_cwise (shell, speed = "linear", length):
    """
    Rotation of the RTT stage, clockwise, units in degrees/

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length: length of motion in degrees. The function makes it negative, as that's the clockwise direction.
    :return:
    """
    rot = "&1 cpx " + speed + "C" + str(-length) + "\n"
    shell.send(rot)

    return()

def rot_ccwise (shell, speed = "linear", length):
    """
    Rotation of the RTT stage, counterclockwise, units in degrees/

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length: length of motion in degrees.
    :return:
    """
    rot = "&1 cpx " + speed + "C" + str(length) + "\n"
    shell.send(rot)

    return()

#A and B axes, rolls and pitche respetively, CS1, units: degrees

def pitchup (shell, speed = "linear", length):
    """
    Tilts the RTT stage towards left, Rotation around Y axis, units: degrees

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length:length of motion in degrees.
    :return:
    """
    pitch = "&1 cpx " + speed + "B" + str(length) + "\n"
    shell.send(pitch)
    return()


def pitchdown (shell, speed = "linear", length):
    """
    Tilts the RTT stage towards right, Rotation around Y axis, units: degrees

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length:length of motion in degrees.
    :return:
    """
    pitch = "&1 cpx " + speed + "B" + str(-length) + "\n"
    shell.send(pitch)
    return ()

def roll_left (shell, speed = "linear", length):
    """
    Tips the RTT stage towards front , i.e. rotation around X axis, units: degrees

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length:length of motion in degrees.
    :return:
    """

    roll = "&1 cpx " + speed + "A" + str(length) + "\n"
    shell.send(roll)
    return()

def roll_right (shell, speed = "linear", length):
    """
    Tips the RTT stage towards front , i.e. rotation around X axis, units: degrees

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param length:length of motion in degrees.
    :return:
    """

    roll = "&1 cpx " + speed + "A" + str(-length) + "\n"
    shell.send(roll)
    return()

