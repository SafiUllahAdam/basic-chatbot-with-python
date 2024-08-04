#Functions , Like in rmeote we can use different buttons for different operations like with '+' button we can perform sound increase.

#similarly in Python, we have different parts of program, every part performs different functions of code 
 
#3 types of functions:  
# 1- In-Built Functions   --  int(), str(), bool()
# 2- Module Functions     -- when related functions and related variable are stored in same file, that file is named as Module in Python e.g we use Math Module ( import math - it has many functions n it we can just call them and use them. To check all we can use print(dir(math)) Now if we want to use square root from math - 1- from math import sqrt or *(for all functions). 2- print (sqrt(16))
# 3- User Defined Functions -- user or programmer made them : syntax - 1- def function_name(parameters) // parameter will be input on basis of which output will be given like in Calculator, Parameter will be operator: ___ 2- //do something in function like make calculator


#Basic Syntax:
#1. Defining a function: Use the * def * keyword.
#2. Calling a function: Use the function's name followed by parentheses '( )' and inside parentheses put values of parameters

def sum(first, sec):
     return (first+sec) #operator for functions

print (sum(5,4))  #values of parameters in Calling the function - Calling the fun means executing it


#User-defined Function: 

def sum(first, sec):
    return first + sec

# Get user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function with user input
#result = sum(num1, num2) if using this storing function in new variable then in next command use this variable reult in place of sum(num1, num2)
print("The sum is:", sum(num1, num2))

 