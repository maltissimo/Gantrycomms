def print_odd(test_list):
    for i in test_list:
        if i % 2 !=0:
            yield i

test_list = [11, 13, 25, 36, 878, 19, 12 ]

print("original list: " + str(test_list))

print("the odd numbers in the list are: ", end = " ")
for j in print_odd(test_list):
    print(j, end=" ")