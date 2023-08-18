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