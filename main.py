import general_comms
import motor_movements
import global_motor_definitions

my_connection  = [0,0]
gantry_init = 0
gantry_homed = 0
loopback = "127.0.0.1"
"""

First things first, create a pmac shell connection

"""
flag = my_connection[1]
if flag == 0:
    my_connection = general_comms.sshCreate()
    flag = my_connection[1]
    ssh = my_connection[0]
else:
    print("Connection already open")

# print(type(ssh))

new_shell = general_comms.connect_to_pmac(ssh)

if gantry_init == 0 and gantry_homed == 0:
    general_comms.GantrySysInit(new_shell)
    global_motor_definitions.home_all(new_shell)
    gantry_init = 1
    gantry_homed = 0
    print("Comms initialised and system homed")

else if gantry_homed == 0 and gantry_init == 1:
    print("Comms already initialised, stand by for system homing.")
    global_motor_definitions.home_all(new_shell)
    print("System homed")

    else if gantry_homed == 1 and gantry_init == 1:
        print("System ready for use")




