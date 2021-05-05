import sys
import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(x, y, action):
    if action == 1:
        score = x + y 
    elif action == 2:
        score = x - y
    elif action == 3:
        score = x * y
    elif action == 4:
        score = x / y
    else:
        logging.debug("Proper action param needed!")
    return score  

def interface():
    #collect initial input
    logging.debug("Enter your data in following order: \n x, y, action_param \n AVILIABLE ACTION PARAMS: \n 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division")
    x = float(input("type x value and hit ENTER: "))
    y = float(input("type y value and hit ENTER: "))
    action = int(input("type action_param and hit ENTER: "))

    value = calculator(x, y, action)
    print(value)

interface()