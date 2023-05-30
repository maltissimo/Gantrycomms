"""
This set of functions is written to make the movements more akin to natural language.
See the definitions of motors in:
global_motor_definitions.py

and the help in
gantry_help.py

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
#(shell, axis, speed, mode, length)


"""
relative motions
"""
#X axis, CS 3, units: microns
def left (shell, length, mode= "inc", speed = "linear"):
    """
    Moves the X head carriage to the left, i.e. positive relative motion.

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length: length of motion in microns
    :return:
    """
    move = "&3 cpx " + mode + " " +  speed + "X" +str(length) +"\n"
    shell.send(move)
    return()

def right (shell, length, mode= "inc", speed = "linear"):
    """
    Moves the X head carriage to the right, i.e. negative relative motion
    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length: length of motion in microns. The function makes it negative.
    :return:
    """
    move = "&3 cpx " + mode + " " +  speed + "X" + str(-length) + "\n"
    shell.send(move)
    return()

#Y axis, CS 3, units:microns

def forward (shell, length, mode= "inc", speed = "linear"):
    """
    Moves the RTT stage foward, i.e. positive relative motion

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length:  length of motion in microns.
    :return:
    """
    move = "&3 cpx " + mode + " " +  speed + "Y" + str(length) + "\n"
    shell.send(move)
    return ()

def back (shell, length, mode= "inc", speed = "linear"):
    """
    Moves the RTT stage back, i.e. negative relative motion

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length: length of motion in microns. The function makes it negative
    :return:
    """
    move = "&3 cpx " + mode + " " +  speed + "Y" + str(-length) + "\n"
    shell.send(move)
    return ()

#Z axis, CS 2, units: microns
def up (shell, length, mode= "inc", speed = "linear"):
    """
    Moves the RTT stage up, i.e. relative positive motion

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length: length of motion in microns.
    :return:
    """
    move = "&2 cpx " + mode + " " +  speed + "Z" + str(length) + "\n"
    shell.send(move)
    return()

def down (shell, length, mode= "inc", speed = "linear"):
    """
    Moves the RTT stage down, i.e. relative positive motion

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length: length of motion in microns. The function makes it negative
    :return:
    """

    move = "&2 cpx " + mode + " " +  speed + "Z" + str(-length) + "\n"
    shell.send(move)
    return()

#Rotation axis, CS 2, units: degrees

def rot_cwise (shell, length, mode= "inc", speed = "linear"):
    """
    Rotation of the RTT stage, clockwise, units in degrees/

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length: length of motion in degrees. The function makes it negative, as that's the clockwise direction.
    :return:
    """
    rot = "&1 cpx " + mode + " " +  speed + "C" + str(-length) + "\n"
    shell.send(rot)

    return()

def rot_ccwise (shell, length, mode= "inc", speed = "linear"):
    """
    Rotation of the RTT stage, counterclockwise, units in degrees/

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length: length of motion in degrees.
    :return:
    """
    rot = "&1 cpx " + mode + " " +  speed + "C" + str(length) + "\n"
    shell.send(rot)

    return()

#A and B axes, rolls and pitche respetively, CS1, units: degrees

def pitchup (shell, length, mode= "inc", speed = "linear"):
    """
    Tilts the RTT stage towards left, Rotation around Y axis, units: degrees

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length:length of motion in degrees.
    :return:
    """
    pitch = "&1 cpx " + mode + " " +  speed + "B" + str(length) + "\n"
    shell.send(pitch)
    return()


def pitchdown (shell, length, mode= "inc", speed = "linear"):
    """
    Tilts the RTT stage towards right, Rotation around Y axis, units: degrees

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length:length of motion in degrees.
    :return:
    """
    pitch = "&1 cpx " + mode + " " +  speed + "B" + str(-length) + "\n"
    shell.send(pitch)
    return ()

def roll_left (shell, length, mode= "inc", speed = "linear"):
    """
    Tips the RTT stage towards front , i.e. rotation around X axis, units: degrees

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length:length of motion in degrees.
    :return:
    """

    roll = "&1 cpx " + mode + " " +  speed + "A" + str(length) + "\n"
    shell.send(roll)
    return()

def roll_right (shell, length, mode= "inc", speed = "linear"):
    """
    Tips the RTT stage towards front , i.e. rotation around X axis, units: degrees

    :param shell: required and active, an SSH shell for comms
    :param speed: linear (i.e. slow) by default. Can be set to rapid
    :param mode: absolute (abs) or relative (inc), set to inc by default
    :param length:length of motion in degrees.
    :return:
    """

    roll = "&1 cpx " + mode + " " +  speed + "A" + str(-length) + "\n"
    shell.send(roll)
    return()

def kill(shell):
    """
    Command to kill all movements at once.
    :param shell: a paramiko shell to the pmac
    :return:
    """
    shell.send("&*abort\n")
    return()

def get_jogspeed(shell, axis):
    """
    Gets from the system the jogspeed for the specified axis
    the user can input in normal x,y,z, pitch, roll, rot  | yaw
    :param shell: a shell connection to the pmac
    :param axis: the axis for which the jogspeed is required
    :return: jogspeed, the programmed jogspeed
    """
    # TODO disable echoing, so as to return only one value, see Pmac user and software manual (page 1154)
    # go on the machine, check with echo what the output is, then set the echo bit according to that, so as to get a response
    # like:
    # Motor[1].JogSpeed
    # 8900
    new_ax = axis_conversion(axis)
    shell.send("Motor[", new_ax, "].JogSpeed")
    out = listen(shell)
    jogspeed = get_value(out)

    return (jogspeed)


def set_jogspeed(shell, axis, value):
    """
    Sets the jog speed of the specified axis, and prints it out for checking  by the user

    :param shell: a shell connection tothe
    :param axis: the axis for which the jogspeed is required
    :param speed: desired jogspeed
    :return
    """
    new_ax = axis_conversion(axis)
    shell.send("Motor[", new_ax, "].JogSpeed=", value)
    newspeed = get_jogspeed(shell, axis)
    output = ""
    output += "The new jogspeed has been set to: " + str(newspeed)
    return (output)