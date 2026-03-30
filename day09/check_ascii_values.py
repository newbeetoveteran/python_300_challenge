# ASCII values
# Concept : Using .isascii(), forcing valid user input using while

user_input = ""

# Using .strip() for checking whitespaces in string

while not user_input.strip():
    user_input = input("Enter the string: ")
    if not user_input.strip():
        print("No valid input found. Please try again.")

# Assigning aggregator variable and list to store the output

ascii_count = 0
ascii_list = []
for char in user_input:
    if char.isascii():
        ascii_list.append(char)
        ascii_count += 1
print(f"Total ASCII count: {ascii_count}")
print(f"Ascii elements: {' '.join(ascii_list)}")