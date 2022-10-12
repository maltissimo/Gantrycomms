"""
This file contains utilities to connect to the Gantry Power Pmac
it uses the paramiko library to open an ssh communication line.

Author M. Altissimo c/o Elettra Sincrotrone Trieste SCpA.

"""
# this is now the loopback interface for testing purposes MA20220810
import paramiko
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
The displacement of the rotary axes is expressed in
degree units.
"""
GPASCII = "gpascii -2"  # this is needed to start the interpreter on the Pmac
EOT = "\04"             #End of transmission character, to close connection
X = 5  # Coordinate system 3, units: microns
Y= 6   # Coordinate system 3, units: microns
Z = "Z"  # Coordinate system 2, moves the RTT stage up and down, units: microns
Roll = "A"  #  tips the RTT stage towards front or back, i.e. rotation around X axis, units: degrees
Pitch = "B" # tilts the RTT stage towards left and right, Rotation around Y axis, units: degrees
Rot = "C"  # rotation around Z axis, units: degrees

ssh = paramiko.SSHClient()

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


def connect_to_pmac():
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
    return(pmac_shell)

def GantrySysInit(shell_connection):
     shell_connection.send("terminal length 0\n")
     shell_connection.send(GPASCII)
     sleep(0.5)
     print(shell_connection.recv(5000).decode("UTF-8"))
     return()

def listen (shell_connection):
    """
    This function returns a bytes output of whatever the shell passed as pararameter contains.

    :param shell_connection: a paramiko active shell object
    :return output: a bytes object ready to be formatted and

    """
    while shell_connection.recv_ready(): #there is space and scope here to add a timeout
        if shell_connection.recv_ready(): # must test for recv_ready() in order for the code not to hang!
            output = shell_connection.recv(1024).decode("UTF-8")

    return(output)

def format_output(bytes_buffer):
    """
    Formats the output of a shell.recv()command.
    :param bytes_buffer: output from the function listen

    """
    delim = "\r\n"
    lines = bytes_buffer.split(delim)
    if not bytes_buffer.endswith(delim):
        bytes_buffer = lines [-1]
        lines = lines[:-1]
    for line in lines:
        yield line.rstrip()

def printout(output):
    """
    This function prints the 1024 bytes of output obtained from the listen(shell) function, and formatted by the format_output(bytes_buffer) output

    :param output: the list formatted by the format_output(bytes_buffer function)
    :return:
    """
    for i in format_output(output):
        print(i, end ="\n")
    return()


def close_connection(SSH_object):
    """
    This is just a wrapper for closing the ssh connection to pmac,
    :SSH_object:  an instance of the SSHClient() class,i.e. a connection
    :return: nothing
    """
    SSH_object.close()
    print("SSH connection successfully closed")
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
    See motor definition above!!!
    The system of reference is inferred from the motor called.
    
    :param axis: axis for motion
    :param speed: interpolated (i.e. slow, pmad default) or rapid.
    :param mode: absolute (abs) or relative (inc)
    :param length: length of motion
    :return: a string containing the move, to be passed to a shell.
    """
    if axis == "X" or  axis == "Y":
        SR = str(3)
    else:
        if axis == "Rot" or axis == "Pitch" or axis == "Roll" or axis == "Z":
         SR = str(2)

    if mode == "relative":
        mode == "rel"

    else: mode == "abs"

    command = "&" + SR + " cpx " + speed + " " +  mode + " " + axis + length + "\n"

    return(command)

def home_all(pmac_conn):
    """
    This function homes all axes as per QSys protocol. It should be run only once the system is turned on.
    :return:
    """
    axes = "selectAxes = selectAll"
    pmac_conn.send(axes)
    home = "requestHost = requestHome"
    pmac_conn.send(home)
    return ()

def axis_conversion(axis):
    """
    Converts axis as input by user back into pmac understandable format

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



def get_jogspeed(axis):
    """
    Gets from the system the jogspeed for the specified axis
    the user can input in normal x,y,z, pithc, roll, rot  | yaw
    :param axis: the axis for which the jogspeed is required
    :return: int, the programmed jogspeed.
    """
    # TODO disable echoing, so as to return only one value, see Pmac user and software manual
    new_ax = axis_conversion(axis)
    if new_ax == "A" or new_ax == "B" or new_ax == "C":
        stdin, stdout, stderr = ssh.exec_command("Motor[1].JogSpeed")
        stdin, stdout, stderr = ssh.exec_command("Motor[2].JogSpeed")
        stdin, stdout, stderr = ssh.exec_command("Motor[3].JogSpeed")
    else:
        stdin, stdout, stderr = ssh.exec_command("Motor[",new_ax,"].JogSpeed")
    return(stdin)

def set_jogspeed(axis):
    """
    sets the jog speed of the specified axis
    """


#TODO: must read data from pmac, i.e.: command finished, standard errors.
#TODO: insert helper function printing names of axes, and units.