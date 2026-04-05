# Count substring
# Concept : using .count(), edge case handling.

user_input = " "
target_substring = " "
while not user_input.strip():
    user_input = input("Enter the string for check: ")
    if not user_input.strip():
        print("No valid input found. Try again.")
while not target_substring.strip():
    target_substring = input("Enter the target substring:")
    if not target_substring.strip():
        print("Please enter the target substring for check.")

substring_count = user_input.count(target_substring)

if substring_count == 0:
    print(f"Target substring not in user input.")
else:
    print(f"{target_substring} appeared {substring_count} times.")