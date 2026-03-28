# Remove punctuation and ASCII values
# Concept: strings, isascii() and 

import string

user_input = input("Enter the sentence/string: ")

if not user_input:
    print("No sentence/string found.")

else:
    ascii_count = 0
    ascii_list = []
    punctuation_count = 0
    punctuation_list = []

    for char in user_input:
        if char.isascii():
            ascii_count += 1
            ascii_list.append(char)
        if char in string.punctuation:
            punctuation_count += 1
            punctuation_list.append(char)
    print(f"Total punctuation count is: {punctuation_count} and total ASCII count is: {ascii_count}")
    print(f"ASCII list is: {' '.join(ascii_list)} and Punctuation list is: {' '.join(punctuation_list)}")