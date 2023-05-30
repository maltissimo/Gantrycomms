def set_meas_data():
    print("Please input the length of the measurement, in mm: ")
    length = float(input())
    print("Would you like to specify your measurement by nr of points (p) or step size(s)?")
    choice = str(input())
    if choice == "p":
        print("please enter the number of points for your measurement: ")
        nr_points = int(input())
        return([length, nr_points, choice])
    elif choice == "s":
        print("Please enter the stepsize of your measurement, in mm: ")
        step_size = float(input())
        return([length, step_size, choice])