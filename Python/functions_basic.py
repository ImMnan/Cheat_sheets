def message():
    print("Enter a value: ")
 
message()
a = int(input())
message()
b = int(input())

print(a + b)


def hello(name): # defining a function
    print("Hello,", name) # body of the function
 
 
name = input("Enter your name: ")
 
hello(name) # calling the function


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")
 

#An example of a three-parameter function:
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)
 
s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)

# Global method to extend a variable's scope in a way which includes the function's body
def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

# changing the parameter's value doesn't propagate outside the function
#This also means that a function receives the argument's value, not the argument itself. This is true for scalars.

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    printprint("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
# Multi-parameter based functions:
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
 
def bmi(weight, height):
    return weight / height ** 2
 
 
print(bmi(52.5, 1.65))