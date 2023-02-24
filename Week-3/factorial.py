#!/usr/bin/env python3
#This is a single line comment
#Python programme to illustrate the user of operaters
#Name :Lydia Wambui
#Email : githuthalydia@gmial.com
#Date : 17th February
#File : factorial.py

#write a programme to calculate the factorial of a number
import math
def factorial(n):
    return(math.factorial(n)) 
num = int(input("Enter value of number:"))
f = factorial(num)   
print("factorial of",num,"is",f)