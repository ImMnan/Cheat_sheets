list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# This inconspicuous part of the code described as [:] is able to produce a brand new list.

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

new_list = my_list[1:-1]
print(new_list)

new_list = my_list[3:]
print(new_list)

new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2] 
del my_list[1:3]
print(my_list)