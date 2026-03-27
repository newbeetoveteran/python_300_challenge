# Remove spaces
# Concept: Strings

user_input = input("Enter the string: ")

if " " in user_input:
    print(f"String after whitespace removed: {user_input.replace(' ', '')}")
else:
    print(f"String does not have any whitespace. {user_input}")