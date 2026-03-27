# Count consonant
# Concept: strings and loop

user_input = input("Enter the sentence: ")
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

consonant_count = 0
for char in user_input:
    if char in consonants:
        consonant_count += 1
print(f"Total consonants in your sentence is: {consonant_count}")