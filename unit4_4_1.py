import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(x, y, action, z):
    if action == 1:
        sum_z = sum(z)
        score = x + y + sum_z
    elif action == 2:
        score = x - y
    elif action == 3:
        mult_z = multiplyList(z)
        score = x * y * mult_z
    elif action == 4:
        score = x / y
    else:
        logging.debug("Proper action param needed!")
    return score  

def interface():
    #collect initial input
    logging.debug("Enter your data in following order: \n x, y, action_param \n AVILIABLE ACTION PARAMS: \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division")
    x = input("type x value and hit ENTER: ")
    y = input("type y value and hit ENTER: ")
    action = input("type action_param and hit ENTER: ")
    z = []
    if action == 1 or 3:
        my_bool = True
        while my_bool == True:
            z_ = input("If you want to add an extra value, type it and hit ENTER \n else hit ENTER: ")
            if z_ is "":
                break
            else:
                z.append(z_)
    check(x, y, action, z)


    




def check(x, y, action, z):
    #check initial input
    if float(x):
        float(x)
    else:
        logging.debug("x is not a number")
        interface()

    if float(y):
        float(y)
    else:
            logging.debug('y is not a number') 
            interface()

    if int(action):
        int(action)
    else:
        logging.debug("param out of range")
        interface()

    z_float = []
    for num in z:
        if float(num):
            float(num)
            z_float.append(z)
        else:
            logging.debug("all values must be numbers")
            interface()

    #call calculator()
    value = calculator(x, y, action, z_float)
    print(value)

interface()

#logging.debug(f"program param is {sys.argv[1:]}")

