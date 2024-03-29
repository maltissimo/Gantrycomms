"""
This file contains utilities to connect to the Gantry Power Pmac
it uses the paramiko library to open an ssh communication line, and creates a shell.
Commands are sent to the Pmac via
shell.send(command)

Author M. Altissimo c/o Elettra Sincrotrone Trieste SCpA.

"""


# this is now the loopback interface for testing purposes MA20220810
import paramiko
#from gantry_help import *
from global_motor_definitions import *
#from motor_movements import *
import time

""" 
GlobalMotor definitions (please check before running!!)

From QSYS manual: 
The linear motion axes are referred to as X, Y and Z. 
The displacement of the linear axes is expressed in micrometer units.
The rotary motion axes are referred to as the A, B and C-axis. The A-axis is the rotation
around the X-axis, with the direction defined by the righthand rule (a clockwise turn when
looking in the positive linear direction). Similarly, the B-axis and the C-axis are the rotation
around the Y and Z-axis respectively. 
The displacement of the rotary axes is expressed in degree units.
"""
GPASCII = "gpascii -2 2>&1\n"  # this is needed to start the interpreter on the Pmac
EOT = "\04"  # End of transmission character, to close connection
X = 5  # Coordinate system 3, units: microns
Y = 6  # Coordinate system 3, units: microns
Z = "Z"  # Coordinate system 1, moves the RTT stage up and down, units: microns
Roll = "A"  #  Coordinate system 1, tips the RTT stage towards front or back, i.e. rotation around X axis, units: degrees
Pitch = "B"  #  Coordinate system 1, tilts the RTT stage towards left and right, Rotation around Y axis, units: degrees
Rot = "C"  #  Coordinate system 2, rotation around Z axis, units: degrees

def sshCreate():
    """
    This creates an SSH client using the paramiko interface. I am writing this as I want one and only one ssh client.

    :return: a paramiko object and a flag set to 1.
    """
    flag = 1
    return([paramiko.SSHClient(), flag])

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
    return ([pmac_ip, pmac_uname, pmac_pwd])


def connect_to_pmac(ssh):
    """
    This functions connects to PMAC and returns a shell object, which can be used to send
    commands down to the PMAC. See file "paramiko_tests.py" for clarification.
    :return pmac_shell: a shell from paramiko, that can be used to send commands down.
    """
    # Load SSH host keys.
    ssh.load_system_host_keys()
    # Add SSH host key when missing.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    credentials = get_credentials()
    ssh.connect(credentials[0], username=credentials[1], password=credentials[2])
    print("Successfully connected to ", credentials[0])
    pmac_shell = ssh.invoke_shell()
    return (pmac_shell)


def GantrySysInit(shell_connection):
    shell_connection.send(GPASCII)
    time.sleep(0.5)
    out = listen(shell_connection)
    printout(out)
    return ()

def listen(shell_connection, nbytes=1024):
    """
    This function returns a bytes output of whatever the shell passed as pararameter contains.

    :param shell_connection: a paramiko active shell object
    :param nbytes: number of bytes to be listened to, default is 1024
    :return output: a bytes object

    """
    while shell_connection.recv_ready():  # there is space and scope here to add a timeout
        if shell_connection.recv_ready():  # must test for recv_ready() in order for the code not to hang!
            output = shell_connection.recv(nbytes).decode("UTF-8")

    return (output)


def format_output(bytes_buffer):
    """
    Formats the output of a shell.recv()command.
    :param bytes_buffer: output from the function listen

    """
    delim = "\r\n"
    lines = bytes_buffer.split(delim)
    if not bytes_buffer.endswith(delim):
        bytes_buffer = lines[-1]
        lines = lines[:-1]
    for line in lines:
        yield line.rstrip()


def printout(output):
    """
    This function prints the bytes of output obtained from the listen(shell) function.
    The usage should be as follows:
    shell.send("mycommand\n")
    out = listen(shell)
    printout(out)

    :param output: the list formatted by the format_output(bytes_buffer function)
    :return:
    """
    for i in format_output(output):
        print(i, end="\n")
    return ()


def get_value(bytes_buffer):
    """
    This function reads the value of a specific parameter (i.e. Motor[x].JogSpeed) and returns it for further use.
    The procedure is shortened, as the split(delim) returns the shell prompt as last value, so we pick the second last.

    :param bytes_buffer: the bytes output of listen(shell)
    :return: a float
    """
    delim = "\r\n"
    lines = bytes_buffer.split(delim)
    return (float(lines[-2]))


def close_connection(SSH_object):
    """
    This is just a wrapper for closing the ssh connection to pmac,
    :SSH_object:  an instance of the SSHClient() class,i.e. a connection
    :return: nothing
    """
    SSH_object.close()
    print("SSH connection successfully closed")
    return ()


def is_open(SSH_object):
    """
    Checks if the connection is still active or not
    Uses the get_transport() function to gain access to the Transport members in paramiko.
    :param SSH_object: an instance of the SSHClient() class,i.e. a connection
    :return: True in case the connection is active, an error if it isn't
    """
    ret = SSH_object.get_transport().is_active()
    return (ret)





