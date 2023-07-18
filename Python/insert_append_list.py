numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)
print(len(numbers))
print(numbers)

###
numbers.insert(0, 222)
print(len(numbers))
print(numbers)


print("\n Creating an empty list with append")
my_list = []  

for i in range(5):
    my_list.append(i + 1)

print(my_list)

print("\n Creating an empty list with insert")
my_list1 = []  
 
for i in range(5):
    my_list1.insert(0, i + 1)
 
print(my_list1)
 