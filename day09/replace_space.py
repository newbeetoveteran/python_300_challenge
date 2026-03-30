#  Replace space with _
#  Concept : Using loops and .isascii()

user_input = " "

while not user_input.strip():
    user_input = input("Please enter the string: ")
    if not user_input.strip():
        print("No valid input found. Please try again.")

replaced_char = user_input.replace(" ", "_")
print(f"Your input after conversion: {replaced_char}")
