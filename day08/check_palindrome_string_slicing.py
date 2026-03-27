# Check palindrome
# Concept: Strings and slicing

user_input = input("Enter the string: ")

reverse_string = user_input[::-1]
print(f"Reversed string : {reverse_string}")

if user_input == reverse_string:
    print("Palindrome!")
else:
    print("Not Palindrome..")