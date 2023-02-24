#advanced data types
#mutable vs immutable
#mutable-data types that can be edited during programm life cycle 
         #can add/remove elements
#immutables-->can not be edited
#1.Lists(mutable)
friends = ["Ruth","Hope","Jeff","Peter"]
#OR friends = []-for empty list
#to remove-del,pop
#to add -append,extend
students = ["michael","Jane","Mercy"]
friends.extend(students)
friends.append("Dennis")
friends.sort()
#2.Tuples(immutable)
#type of list that can not be edited
stationary = ("ink","pens","eraser","pencil")

stationaries = ("ruler","clickboard")
for stationary in stationaries:
    print(stationary)
    
#3.Dictionaries aka dict
#uses key and value pair to store data
#name->(key) Lydia->(value)
student = {"name" : "Lydia","age":19,"gender":"female"}
print(student["name"])
print(student["age"])
print(student["gender"])

#sets
my_fruits = {"banana","orange","peach","melon","quava"}
for fruit in my_fruits:
    print(fruit)
    print(len(my_fruits))
   #divided into ordered(similar data types)&non ordered(different data types)
    