def imported(modulename):
    if not (str(modulename) in sys.modules):
        print("The module "+ str(modulename) + " successfully imported")
    else:
        print("ERRROR! The module "+ str(modulename) + "has not been imported, try a manual import")

    return()

sys = __import__("sys")
imported(sys)
os = __import__("os")
imported(os)
motor_movements = __import__("motor_movements")
imported(motor_movements)
np = __import__("numpy")
imported(np)
testing_gimport = __import__("testing_gimport")
imported (testing_gimport)





