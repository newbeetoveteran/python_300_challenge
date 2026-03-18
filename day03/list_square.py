# Create square list
# Concept : loop and value accumulator list

# Taking user input to populate list

user_list = []
for i in range(4):
    user_input = int(input(f"Enter the elements in list {i+1}: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Assining an empty list
# Populating square of the elements in list by iterating through all elements

square_list = []
for element in user_list:
    square_list.append(element * element)
print(f"Square of the list is: {square_list}")