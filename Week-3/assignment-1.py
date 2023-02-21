#!/usr/bin/env python3
#This is a single line comment
#Python programme to illustrate the user of operaters
#Name :Lydia Wambui
#Email : githuthalydia@gmial.com
#Date : 17th February
#File : assignment-1

myFavouriteMusicians = []
myFavouriteMusicians = ["marverick city","Mercy masika","Rihanna","Travis greene","Guardian angel"]
for musician in myFavouriteMusicians:
    print(musician)
updatedmusicians = myFavouriteMusicians + ["burna boy","Tems","ed sheeran","calvin harris","coldplay"]
for musician in updatedmusicians:
    print(musician)
celebs = updatedmusicians.copy()    
print(celebs)
celebs.sort()
print(celebs)
celebs.pop()
print(celebs)
celebs.pop()
print(celebs)
print(len(celebs))


