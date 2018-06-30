# -*- coding: utf-8 -*-
"""
Created on Wed May 30 13:54:46 2018

@author: Vishwesh Ravi Shrimali
"""

# Define functions

def add(numList):
    return numList[0]+numList[1]

def sub(numList):
    return numList[0]-numList[1]

def mult(numList):
    return numList[0]*numList[1]

def div(numList):
    returnVal = 'error'
    try:
        returnVal = numList[0]/numList[1]
    except ZeroDivisionError:
        print("Division by zero is not defined.")
    return returnVal

def square(numList):
    return numList[0]**2

def sqrt(numList):
    if numList[0] < 0:
        print("You are trying to find out square root of a negative number. The program will result in a complex number.")
    return numList[0]**0.5

# Define list of functions
operations = [add,sub,mult,div,square,sqrt]
# Define list of number of args
numArgs = [2,2,2,2,1,1]

def selectMode():
    print("Select one of the following calculation modes:")
    print("1\tAddition\n2\tSubtraction\n3\tMultiplication\n4\tDivision\n5\tSquare a number\n6\tSquare root of a number\n")
    mode = input("Enter option number (eg. 1, 2): ")
    # Only first letter is relevant
    mode = mode.strip()
    while mode not in [str(i) for i in range(1,7)]:
        print("Invalid choice. Try again")
        mode = input("Enter option number (eg. 1, 2): ")
    return int(mode)

def continueOrStop():
    choice = input("Enter Q to quit the program. Enter any other letter to continue: ")
    if choice.strip().lower() == 'q':
        return 0
    else:
        return 1

def validInput(inp):
    inp = inp.strip()
    try:
        inp = float(inp)
    except:
        print("Non-numeric input detected. Try again.")
        return -1
    return 0

def callFunction(mode):
    mode = mode-1
    print("You selected %s mode"%(operations[mode].__name__))
    print("This mode requires %d inputs"%(numArgs[mode]))
    inputs = []
    for i in range(numArgs[mode]):
        num = input("Enter number: ")
        while validInput(num)==-1:
            num = input("Enter number: ")
        inputs.append(float(num))
    print("Answer =",(operations[mode](inputs)))

# Exceptions to take care of
## Non-numeric input - ValueError
## Division by zero: ZeroDivisionError
## Square root of negative number - Going on with complex number
def main():
    print("------Welcome to Python Calculator------")
    continueProg = 1
    while continueProg:
        mode = selectMode()
        callFunction(mode)
        continueProg = continueOrStop()
    print("------Thank you------")

if __name__ == "__main__":
    main()