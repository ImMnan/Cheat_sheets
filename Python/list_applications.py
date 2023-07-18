my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

print("\n Easily swap the list's elements to reverse their order")
my_list1 = [10, 1, 8, 3, 5]
 
my_list1[0], my_list1[4] = my_list1[4], my_list1[0]
my_list1[1], my_list1[3] = my_list1[3], my_list1[1]
 
print(my_list1)

print("\n Doing the same with for loop")

length = len(my_list1)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)
 