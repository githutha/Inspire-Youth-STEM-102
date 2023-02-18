#!/usr/bin/env python3
#This is a single line comment
#Python programme to illustrate the user of operaters
#Name :Lydia Wambui
#Email : githuthalydia@gmial.com
#Date : 17th February
#File : bank.py


#write a programme that calculates : 
#16% tax on income ranging btw 100k-150k
#19% tax if your income is btw 150k-300k
#30% tax if your income is above 300k
#5% tax if income is less 100k
#print gross income and net income

#formula gross_income = net income + taxes
# formula net income = gross ncome - taxes


#above 300k
income1 = int(input("enter income 1:"))
if(income1 >=300000):
    gross_income1 = income1 + ((30/100 )* income1)
    net_income1 = income1-((30/100)*income1)
    print("Your income is {} hence your gross income1 is {}" .format(income1,int(gross_income1)))
    print("Your income is {} hence your net income1 is {}" .format(income1,int(net_income1)))

#150k to less than 300k
income2 = int(input("Enter income 2:"))
if(income2 >= 150000) & (income2 < 300000): 
    gross_income2 = income2 + ((19/100)*income2)
    net_income2 = income2-((19/100)*income2)
    print("Your income2 is {} hence your gross income is {}" .format(income2,int(gross_income2)))
    print("Your income 2 is {}hence your net income 2 is {}" .format(income2,net_income2))

#100k to less than 150k
income3 = int(input("Enter income 3:"))
if(income3 >= 100000) & (income3 < 150000):
    gross_income3 = income3 + ((16/100) * income3)
    net_income3 = income3-((16/100)*income3)
    print("Your income 3 is {} hence your gross income 3 is {}" .format(income3,int(gross_income3)))
    print("Your income 3 is {} hence ypur net income 3 is {}" .format(income3,int(net_income3)))

#less than 100k
income4 = int(input("Enter income 4:"))
if(income4 >=1) & (income4 < 100000): 
    gross_income4 = income4 + ((5/100)* income4)
    net_income4 = income4 - ((5/100)*income4) 
    print("Your net income 4 is {} hence your gross income 4 is {}" .format(income4,int(gross_income4)))
    print("Your income 4 is {} hence your net income 4 is {}" .format(income4,int(net_income4)))


