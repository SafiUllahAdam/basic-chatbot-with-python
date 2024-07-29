 #All data-types we studies till now int, float, string were Primitive data-types
 #(Primitive)These are the most basic data structures and serve as the building blocks for data manipulation.
 #(List data-types)These are more complex structures that include We can save multiple primitives in it: List, tuple, array, dictionaries
 
#To store marks in list named marks

marks = [80, 70, 75]
print("Your marks of Physics are", marks[0]) #80
marks = [80, 70, 75]
print("Your marks of Chem are", marks[-2]) #70 - means starting index from ending of list
marks = [80, 70, 75]
print("Your total marks are", marks[0:2]) #exculding 2

#Now for loop 

marks = [80, 70, 75]
marks.append(99) #only joining at end, to join any value in random place like in-between the list then we use insert 
marks.insert(0,99)
for score in marks: #for item in range()
 print(score)
print(99 in marks) #to check whether newly append or inserted value exists in list or not / if exists it returns true

print(marks)
print("Length of your list is : " , len(marks))

#Now While loop

marks1=[60, 70, 80]

i=0
while i < len( marks1):
    print (marks1[i])
    i=i+1