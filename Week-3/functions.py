#block of code that are executed together
#functions use -def keyword
def print_name():
    print("My name is Lydia")
    print("I am 19 years old")
    print("I live in Nairobi")
    print("My hobby is swimming")
    print("I enjoy travelling")

#calling the function  
print_name()  

def add_numbers(num1,num2):
    sum_num = num1+num2
    print(sum_num)
add_numbers(20,50)
add_numbers(70,36)
add_numbers(45,89)

def mult_numbers(num1,num2):
    prod_num = num1 * num2
    print(prod_num)
    mult_numbers(27,82)
