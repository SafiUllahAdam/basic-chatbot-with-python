#Let's make a program which continuously inputs a number and tells if that number is an odd or even number. If the user enters a negative number the program stops.

value=int(input("Enter the Value : "))


while value>0:
    if (value%2) == 0:
        print("The Number you enter " ,value, "is EVEN")
    else:
        print("The Number you enter " ,value, "is ODD")
        
    value=int(input("Enter the Value : ")) # to save yourself from running the code again & again and checking even or odd numbers, we have to put user input value again after loop. This will also break the continous cycle of loop in case of condition met
    
print("OOPS The Number you enter " ,value, "is Negative. Please Enter a Positive Number")