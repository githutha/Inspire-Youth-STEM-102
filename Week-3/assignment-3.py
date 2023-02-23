#!/usr/bin/env python3
#This is a single line comment
#Python programme to illustrate the user of operaters
#Name :Lydia Wambui
#Email : githuthalydia@gmial.com
#Date : 17th February
#File : assignment-3

# using for loop draw a diamond triangle pascals table
R = int(input("Enter the range:"))
for diamond in range(R):
    print(" " *(R - diamond), " *" * (2* diamond + 1))
for diamond in range(R-2,-1,-1):
    print(" " *(R - diamond)," *"   *(2 * diamond + 1))

print("-----------------------------------------------------")     

    #display a triangle with for loop
a = int(input("Enter number:")) 
y = a-1
for i in range(1,a+1):
        space = " " * y
        stars = "* " * i
        print(space + stars)
        y = y-1

#pascals table
from math import factorial
#input n
n =8
for i in range(n):
     for j in range(n-i+1):
         print(end=" ")
     for j in range(i+1):
       print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ") 
     print()       