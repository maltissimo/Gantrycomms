"""
This module provides a set of helper functions, to be used in conjuction with the rest of the module.

Author M. Altissimo c/o Elettra Sincrotrone Trieste SCpA.

"""
import ast
import os


def help_credentials():
    """
    Prints connection credentials for ssh-ing into pmac
    :return: IP, username and pwd of pmac
    """
    print("Pmac IP:         192.168.0.200")
    print("Pmac username:   root")
    print("Pmac Password:   deltatau")
    print()
    print("You are welcome!")
    return()

def help_units ():

    """
    Prints the standard units of measurement for the Gantry.

    :return:
    """

    print("These are the STANDARD units of measurement for the axes in the Gantry: ")
    print()
    print(" Axis             Units")
    print("   X             microns  ")
    print("   Y             microns  ")
    print("   Z             microns  ")
    print(" Pitch           degrees  ")
    print("  Roll           degrees  ")
    print("  Yaw            degrees  ")
    return()

def help_reference():
    """
    Prints the axes, their number convention in the system, and the System of Reference (SR) they belong to.

    :return:
    """
    print("These are the built-in axes to number and the Coordinate System (CS) conventions")
    print()
    print(" X = 5,    Coordinate System: 3, units: microns")
    print(" Y = 6,    Coordinate system: 3, units: microns")
    print(" Z = Z,    Coordinate system: 2, moves the RTT stage up and down, units: microns")
    print("Roll = A,  Coordinate System: 1, tips the RTT stage towards front or back, i.e. rotation around X axis, units: degrees")
    print("Pitch = B, Coordinate System: 1, tilts the RTT stage towards left and right, Rotation around Y axis, units: degrees")
    print("Rot = C,   Coordinate System: 1, rotation around Z axis, units: degrees")
    return()

def help_move()

    """
    Prints the help for issuing a move command from the shell, as combined via gantry.sh and get_moving.py
    :return: 
    """

    print("The correct syntax for the move is as follows ")
    print("gantry COMMAND TYPE NUMBER\n")
    print("where: ")
    print("\"gantry\" calls the executable shell script, which in turns invokes the python code")
    print("\"COMMAND\" refers to a specific movement, and can be set to: ")
    print("left, right, forward, backward up, down, rot_cwise, rot_ccwise, pitchup, pitchdown")
    print("\"TYPE\" is either RELATIVE (rel) or ABSOLUTE (ABS) ")
    print("\"NUMBER\" is either the relative distance or the absolute coordinate for the specific movement")
    print("by default, the speed is set to \"linear\", i.e. slow ")
    return()

