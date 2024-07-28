
#Conditional statements ( IF-THEN , IF-ELSE)

num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))

#Now we will use conditional statement & check which number is bigger from either.

if (num1 > num2):
    print("The First number", num1, "is Greater than Second Number", num2)
else:
    print("The Second number", num2, "is Greater than First Number", num1)


#PROGRAM 1 - Calculate grades of students

print("WELCOME TO AI-GRADERS : CALCULATE YOUR GRADES")
english=int(input("Enter your marks of English : "))
maths=int(input("Enter your marks of Maths : "))
urdu=int(input("Enter your marks of Urdu : "))
sum= english+maths+urdu
avrg=(sum/3)

print("The Average Marks of your all 3 subjects = " , avrg)

if (avrg>50):
    print("Your Average marks are more than 50, So Congratulations You have Passed the Semester ")
else:
    print("OOPS! Your Average marks are less than 50, So Unfortunately You have Failed the Semester ")


