def imported(modulename):
    test = str(modulename)
    test2 = test.split(sep = " ")
    if not (str(modulename) in sys.modules):
        print("The module "+ str(test2[1]) + " has been successfully imported")
    else:
        print("ERRROR! The module "+ str(test2[1]) + "has not been imported, try a manual import")

    return()

sys = __import__("sys")
imported(sys)

os = __import__("os")
imported(os)

paramiko = __import__("paramiko")
imported(paramiko)

motor_movements = __import__("motor_movements")
imported(motor_movements)

global_motor_definitions = __import__("global_motor_definitions")
imported(global_motor_definitions)

gantry_help = __import__("gantry_help")
imported(gantry_help)

general_comms = __import__("general_comms")
imported(general_comms)
"""
The py file is empty, so it causes an error.

error_list = __import__("pmac_error_list.py")
imported(error_list)
"""
time = __import__("time")
imported(time)

ast = __import__("ast")
imported(ast)


