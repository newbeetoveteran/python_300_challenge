# Remove first occurrence
# Concept : strings, loops and flag

user_input = " "
target_char = " "

while not user_input.strip():
    user_input = input("Enter the string: ")
    if not user_input.strip():
        print("No valid input found. Please try again.")

while not target_char.strip():
    target_char = input("Enter the target char to be removed: ")
    if not target_char.strip():
        print("Please enter a valid character.")

removed = False
result = ""

for char in reversed(user_input):
    if char == target_char and not removed:
        removed = True
        continue
    result += char
result = result[::-1]
print(f"Result after removing last occurrence: {result}")
