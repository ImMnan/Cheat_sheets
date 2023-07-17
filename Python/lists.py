numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.
 
numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.

del numbers[1]
print("Deleted the seconde entity in the list: ", numbers)
print("Remaining items in the list are ", len(numbers))

#Example second:

num = [10, 5, 7, 2, 1]
print("\n \n Original list contents:", num,)  # Printing original list contents.

num[0] = 111
print("Previous list contents:", num)  # Printing previous list contents.

num[1] = num[4]  # Copying value of the fifth element to the second.
print("Previous list contents:", num)  # Printing previous list contents.

print("\nList length:", len(num))  # Printing the list's length.
