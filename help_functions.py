"""
This module provides a set of helper functions, to be used in conjuction with general_comms.py.

Author M. Altissimo c/o Elettra Sincrotrone Trieste SCpA.

"""


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
    print("These are the default axes to number and the Coordinate System (CS) conventions")
    print()
    print(" X = 5,    Coordinate System:  3")
    print(" Y = 6,    Coordinate system: 3")
    print(" Z = Z,    Coordinate system: 2, moves the RTT stage up and down")
    print("Roll = A,  Coordinate System: 1, tips the RTT stage towards front or back, i.e. rotation around X axis")
    print("Pitch = B, Coordinate System: 1, tilts the RTT stage towards left and right, Rotation around Y axis, units: degrees")
    print("Rot = C,   Coordinate System: 1, rotation around Z axis")
    return()