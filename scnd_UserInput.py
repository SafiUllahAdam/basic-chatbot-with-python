#We are going to make a program in python which will ask user 3 Values then add 3 numbers 50, 100, 50 and display their sum.

nameofcust=input("What's Your Name ? ")
print("Good Day", nameofcust)

occupation=input("What is your current Occupation " + nameofcust + " ? " )
print("It's very interesting if you do", occupation,"ing")

print(nameofcust, "Lets Play Some Game to add some numbers")
num1= int(input("Enter 1st Value : "))
num2= int(input("Enter 2nd Value : "))
num3= int(input("Enter 3rd Value : "))
sum= num1 + num2 + num3
#print("Sum of 3 numbers which you enetered: "+num1+num2+num3+ sum)
print("Sum of 3 numbers which you entered: " + str(num1) + " + " + str(num2) + " + " + str(num3) + " = " + str(sum))

