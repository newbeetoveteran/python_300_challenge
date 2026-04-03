# Remove duplicate char
# Concept : loop, dictionary

user_input = " "

while not user_input.strip():
    user_input = input("Enter the sentence: ")
    if not user_input.strip():
        print("No valid input found. Try again")

duplicate_char = {}

for char in user_input:
    if char in duplicate_char:
        duplicate_char[char] += 1
    else:
        duplicate_char[char] = 1

# New string without duplicate char

without_duplicate_string = ""
for char in user_input:
    if duplicate_char[char] == 1:
        without_duplicate_string += char
print(f"Without duplicate character string: {without_duplicate_string}")