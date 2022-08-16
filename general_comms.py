"""
This file contains utilities to connect to the Gantry Power Pmac
it uses the paramiko library to open an ssh communication line.

Author M. Altissimo c/o Elettra Sincrotrone Trieste SCpA.

"""
# this is now the loopback interface for testing purposes MA20220810
import paramiko

""" 
GlobaMotor definitions (please check before running!!)

From QSYS manual: 
The linear motion axes are referred to as X, Y and Z, with the positive direction as shown in
the pictures above. The displacement of the linear axes is expressed in micrometer units.
The rotary motion axes are referred to as the A, B and C-axis. The A-axis is the rotation
around the X-axis, with the direction defined by the righthand rule (a clockwise turn when
looking in the positive linear direction). Similarly, the B-axis and the C-axis are the rotation
around the Y and Z-axis respectively. The displacement of the rotary axes is expressed in
degree units.
"""

X = 5
Y= 6
Z = 3
Roll = "A"  #  rotation around X axis
Pitch = "B" #Rotation around Y axis
Rot = "C" # rotation around Z axis

ssh = paramiko.SSHClient()


def get_credentials():
    """
    This function prompts the user to insert ip, username and password for ssh connection to the system.
    It may be the pmac itself, or a loopback interface for testing purposes.

    :return: three strings to be passed to the connec_to_pmac function, i.e. pmac_ip, pmac_uname, and pmac_pwd
    """
    print("You will be asked to input IP, username and password for ssh connection to the remote system. ")
    print(" It may be the pmac itself, or a loopback interface for testing purposes.")
    print()
    print("Please enter system IP address: ")
    pmac_ip = str(input())
    print("Please enter system username: ")
    pmac_uname = str(input())
    print("Please enter system password: ")
    pmac_pwd = str(input())
    return (pmac_ip, pmac_uname, pmac_pwd)


def connect_to_pmac(pmac_ip, pmac_uname, pmac_pwd):
    """
    This functions connects to PMAC

    :param pmac_ip: Pmac's IP address
    :param pmac_uname: Pmac's user name
    :param pmac_pwd: Pmac's password
    :return: nothing
    """
    # Load SSH host keys.
    ssh.load_system_host_keys()
    # Add SSH host key when missing.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    total_attempts = 5
    for attempt in range(total_attempts):
        try:
            print("Attempt to connect: %s" % attempt)
            # Connect to pmac using username/password authentication.
            ssh.connect(pmac_ip, username=pmac_uname, password=pmac_pwd, look_for_keys=False)
        except Exception as error_message:
            print("Unable to connect, perhaps wrong password?")
            print(error_message)
    return()



def close_connection(SSH_object):
    """
    This is just a wrapper for closing the ssh connection to pmac,
    :SSH_object:  an instance of the SSHClient() class,i.e. a connection
    :return: nothing
    """
    SSH_object.close()
    return()

def is_open(SSH_object):
    """
    Checks if the connection is still active or not
    Uses the get_transport() function to gain access to the Transport members in paramiko.
    :param SSH_object: an instance of the SSHClient() class,i.e. a connection
    :return: True in case the connection is active, an error if it isn't
    """
    ret = SSH_object.get_transport().is_active()
    return(ret)

def move(axis, speed, mode,  length ):
    """
    See motor definition above!!! This sends an exec_command through ssh to the pmac
    The system of reference is inferred from the motor called.
    
    :param axis: axis for motion
    :param speed: interpolated (i.e. slow, pmad default) or rapid.
    :param mode: absolute (abs) or relative (inc)
    :param length: length of motion
    :return: 
    """
    if axis == "X" or  axis == "Y":
        SR = str(3)
    else:
        if axis == "Rot" or axis == "Pitch" or axis == "Roll" or axis == "Z":
         SR = str(2)

    if mode == "relative":
        mode == "rel"

    else: mode == "abs"

    command = "&" + SR + " cpx " + speed + " " +  mode + " " + axis + length

    print(command)
    stdin, stdout, stderr = ssh.exec_command(command)

    return()

def home_all():
    """
    This function homes all axes as per QSys protocol
    :return:
    """
    axes = "selectAxes = selectAll"
    ssh.exec_command(axes)
    home = "requestHost = requestHome"
    ssh.exec_command(home)
    return ()

#TODO: must read data from pmac, i.e.: command finished, standard errors.