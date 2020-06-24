##
## ****************************************************************************
## Maheep Inder Singh
## project 1: Simple Calculator
##*****************************************************************************
##

import check
import math

def helper_function(x,s,y):
    if s == "+":
        y = x + y
        return y
    elif s == "-":
        y = x - y
        return y
    elif s == "*":
        y = x * y
        return y
    elif s == "/":
        y = x / y
        return y


    

def simple_calc(m):
    x = input("Enter Value")
    while x.isdigit() == False:
        print('Invalid input.')
        x = input('Enter Value: ')
    x = int(x)
    
    
    z = input("Enter Operation:")
    while not(len(z) == 1 and (z in "+-*/=")):
        print('Invalid input.')
        z = input('Enter Operation: ')
     
    if z == "=":
        m = m+x
        return m
    else: 
        y = input("Enter Value")
        while y.isdigit() == False:
            print('Invalid input.')
            y = input('Enter Value: ')
        y = int(y)
        return helper_function(x,z,y)


def val(x):
    z = input("Enter Operation:")
    while not(len(z) == 1 and (z in "+-*/=")):
        print('Invalid input.')
        z = input('Enter Operation: ')    
    
    
    
        
def calc():
    '''
    Consumes nothing, returns None, and prints the result of all the operations
    done on all the numbers entered by the user.
    
    effects:
    prompts to the screen and takes user input from keyboard that "Enter Value"
    and "Enter Operation".If the user enters a wrong value 'Invalid input.' is 
    printed and user gets prompted with the same message again until the 
    corrected is entered.
    
    After performing tasks to desirability, when the user enters "=" for
    the final operation, the calculated value is printed on the screen.
    
    calc: None -> None

    '''    
    j = simple_calc(0)
    z = input("Enter Operation:")
    while not(len(z) == 1 and (z in "+-*/=")):
        print('Invalid input.')
        z = input('Enter Operation: ')     
    if z == "=":          
        print(j)
    else:
        
        print(helper_function(simple_calc(0),z,j))
        print("Write calc(), then enter the value displayed above")
    
    
    

