#!/usr/bin/env python3
#This is a single line comment
#Python programme to illustrate the user of operaters
#Name :Lydia Wambui
#Email : githuthalydia@gmial.com
#Date : 17th February
#File : assignment-2.py

#write a programme to solve the quardratic equation
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
d = (b**2)-(4*a*c) #discriminant
print("the value of the discriminant is:",d)
answer1 = (- b + d**0.5/2*a)
print(answer1)
answer2 = (- b - d**0.5/2*a)
print(answer2)
print("the root of this quadratic equation are:",answer1,answer2)
