#  First repeating character
#  Concept : loops and sets

user_input = " "

while not user_input.strip():
    user_input = input("Enter the string: ")
    if not user_input.strip():
        print("No valid input. Try again.")

first_repeating = {}

# Checking character frequency.

for char in user_input:
    if char in first_repeating:
        first_repeating[char] += 1
    else:
        first_repeating[char] = 1

# Checking first repeating character in user_input

for char in user_input:
    if first_repeating[char] > 1:
        print(f"First repeating character is : {char}")
        break
else:
    print("No repating characters in the string found.")