#Write a programm to show odd numbers btw 1 and 100
print("the values below are odd numbers")
for odd_numbers in range(1,101):
    if(odd_numbers%2 !=0):
        print(odd_numbers)
#write a programm to show even numbers btw 1 and 100
print("the values below are even numbers")
for even_numbers in range(1,101):
    if(even_numbers%2 ==0):
        print(even_numbers) 
#write a programm to show prime numbers btw 1 and 100
print("the values below are prime numbers")
for prime_numbers in range(1,101):
    if prime_numbers >1:
        for i in range(2,prime_numbers):
            if(prime_numbers% i) ==0:
                break
        else:
            print(prime_numbers)    
#write a programm to show an arithmetric progression for number btw 1 and 20
n = 10
a=input("enter the first term")
d=input("enter the difference")
arithmetricprogression=(int(a)+(n-1)*int(d))          