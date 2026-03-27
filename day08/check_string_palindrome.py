# Check palindrome
# Concept: Strings and loop

user_input = input("Enter the string: ")

reverse_string = ""

for char in user_input:
    reverse_string = char + reverse_string

print(f"Reversed string: {reverse_string}")
if reverse_string == user_input:
    print("Palindrome!")
else:
    print("Not Palindrome..")
