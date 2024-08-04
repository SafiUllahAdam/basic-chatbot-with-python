# Structures in Python
# 1- List : [] brackets. It can have random and repeating number , we can add , append, remove any number (Single student info)
# 2- Tuple : () brackets(not necessary to use). Values are fixed It can have random and repeating numbers , we cannot change or alter the values
# 3- Set : {} brackets. It can only have unique  numbers , we don;t have index in set so it is called unordered :) 
# 4- Disctioanry {}: To store Key-Value Pair we use dic. In cases where only info of student is not enough and we have to store other info as well like parents details or sblings - Info stored in Pair

marks ={"English" : 99, "Chemistry" : 90, "Physics" : 88}
 
print (marks["English"]) #Instead of index, we can write full keyword
#print (marks.keys()) #To get all keys
 #We can add new Key-Value pair as well
marks["Maths"] = 95;
print(marks) 