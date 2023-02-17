age = 16
gender = "male"

if (age < 18):
    print("You are still young")
else:
    print("You should get an ID")

#compound/multiple conditions
if ((age > 30) & (gender == "male") ):
    print("You qualify for a loan")
else:
    print("No loan for you")        

fav_colour = "blue"
age = 22
if (fav_colour =="blue") | (age <= 20):
    print("Happy birthday to you")
else:
    print("No birthday present for you")    
