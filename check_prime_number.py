# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:46:15 2018

@author: Vishwesh Ravi Shrimali
"""

from math import sqrt

def checkInput(num):
    if num.isdigit():
        if int(num) <= 1:
            print("Number should be more than 1.")
            return "error"
        return int(num)
    else:
        print("Invalid input (Enter a positive integer)")
        return "error"

def getInput():
    print("Welcome to Prime Checker")
    num = input("Enter a positive integer: ").strip()
    while checkInput(num)== "error":
        num = input("Enter a positive integer: ")
    num = checkInput(num)
    if checkPrime(num):
        print("%d is a prime number"%num)
    else:
        print("%d is NOT a prime number"%num)

def checkPrime(num):
    if num==2:
        return True
    elif num%2==0:
        return False
    else:
        for i in range(2,int(sqrt(num))+1):
            if num%i == 0:
                return False
    return True

def main():
    getInput()
    print("Thank you")
    
if __name__ == "__main__":
    main()