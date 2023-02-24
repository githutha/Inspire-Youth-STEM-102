#!/usr/bin/env python3
#This is a single line comment
#Python programme to illustrate the user of operaters
#Name :Lydia Wambui
#Email : githuthalydia@gmial.com
#Date : 17th February
#File : assignment-5

#write a programme to calculate simple interest
P =(input("Enter the value of P:"))
R = (input("Enter the value of R:"))
T = (input("Enter the value of T:"))
def simple_interest(P,R,T):
    S_I = int(P * R * T)/100
    print(S_I)
simple_interest(25000,4,3)
    