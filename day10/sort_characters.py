# Sort characters
# Concept : using sorted and .join()

user_input = " "

while not user_input.strip():
    user_input = input("Enter the string: ")
    if not user_input.strip():
        print("No valid user input found. Try again.")

sorted_string = "".join(sorted(user_input))
print(f"Sorted string: {sorted_string}")