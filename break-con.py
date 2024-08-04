#MAKE A LIST of students then make 2 different scenerios
#Senerio1- Print the name of students till ALI

students = ["Safi", "Eesha", "Ali", "Bilal", "Aliza"]

for student in students:
 if student == "Ali":
  break; #at this point, loop will break and come out of loop and go to next command
 print(student)
 
for student in students:
    if student == "Eesha":
      continue; #at this point, loop will break only on specific value of array and will not come out of loop and completes the value/array then move to next command
    print(student)