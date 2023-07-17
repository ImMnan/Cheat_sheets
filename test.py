word_without_vowels = ""
user_word = input("Enter the word: ")
user_word =  user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        letter += word_without_vowels

print(word_without_vowels)  

