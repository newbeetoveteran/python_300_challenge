#  First non-repeating char
#  Concept: Using dictionary and loop

user_input = " "

while not user_input.strip():
    user_input = input("Enter the string: ")
    if not user_input.strip():
        print("No valid input found. Try again!")

first_non_repeating_char = {}

for char in user_input:
    if char in first_non_repeating_char:
        first_non_repeating_char[char] += 1
    else:
        first_non_repeating_char[char] = 1
print(f"Non repeating set: {first_non_repeating_char}")

for char in user_input:
    if first_non_repeating_char[char] == 1:
        print(f"First non repeating char is: {char}")
        break
else:
    print("No valid non repeating char found.")
