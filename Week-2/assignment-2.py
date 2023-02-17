#write a programm to display a table

#import module
from tabulate import tabulate

#assign data
my_data = [
    ["Michael","Tennis"],
    ["Rose","Volleyball"],
    ["Joshua","Netball"],
    ["Ruth","Football"],
    ["Naomi","Handball"],
    ["Bob","Swimming"],
]

#create header
Head = ["student name","favourite sport"]

#display table
print(tabulate(my_data, headers=Head, tablefmt="grid"))