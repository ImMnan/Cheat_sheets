dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)


#each key must be unique − it's not possible to have more than one key of the same value;
#a key may be any immutable type of object: it can be a number (integer or float), 
# or even a string, but not a list;
#a dictionary is not a list − a list contains a set of numbered values, 
# while a dictionary holds pairs of values;
#the len() function works for dictionaries, too − it returns the number of key-value 
# elements in the dictionary;
#a dictionary is a one-way tool − if you have an English-French dictionary, you can look 
# for French equivalents of English terms, but not vice versa.

print(dictionary['cat'])
print(phone_numbers['Suzy'])

# For looping for validating dictionary elements
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

#Adding a new key-value pair to a dictionary is as simple as changing a value
dictionary['swan'] = 'cygne'
print(dictionary)

del dictionary["dog"]
print(dictionary) # outputs: {}


#  to access a dictionary item,
pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # outputs: soil

item_2 = pol_eng_dictionary.get("woda")    # ex. 2
print(item_2)    # outputs: water

#  to loop through a dictionary's keys and values, you can use the items() method
pol_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
 
for key, value in pol_dictionary.items():
    print("Pol/Eng ->", key, ":", value)

# To copy a dictionary
copy_dictionary = pol_eng_dictionary.copy()

# To delete a dictionary
del pol_eng_dictionary 