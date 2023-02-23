#!/usr/bin/env python3
#This is a single line comment
#Python programme to illustrate the user of operaters
#Name :Lydia Wambui
#Email : githuthalydia@gmial.com
#Date : 17th February
#File : lists_revisited

myFavouriteFruits = ["apple","pineapple","peach","avocado","melon","orange"]
for fruit in myFavouriteFruits :
    print(fruit)

#number of elements
    print(len(myFavouriteFruits))

friends = ["mike","ruth","rose","john","michael","precious"]
print(friends) 
friends[0] = "mark"
print(friends)
print("-----------------------------------")
new_friends = friends.copy()
print(new_friends)
new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)

