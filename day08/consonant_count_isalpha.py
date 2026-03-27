# Count consonant
# Concept: strings and loop

user_input = input("Enter the sentence: ")
vowels = "aeiouAEIOU"

consonant_count = 0
for char in user_input:
    if char.isalpha() and char not in vowels:
        consonant_count += 1
print(f"Total consonants in sentence is: {consonant_count}")