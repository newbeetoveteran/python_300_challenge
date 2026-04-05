#  Swap first & last char
#  concept : slicing and loop - treating entire sentence as a single string

user_input = " "

while not user_input.strip():
    user_input = input("Enter the string: ")
    if not user_input.strip():
        print("No valid input found. Please try again.")

first_char = user_input[0]
last_char = user_input[-1]
swapped_char = user_input[-1] + user_input[1:-1] + user_input[0]
print(f"After swapping first with last: {swapped_char}")
