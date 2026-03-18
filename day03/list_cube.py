# Create cube list
# Concept : loop and value accumulator list

# Taking user input to populate list

user_list = []
for i in range(4):
    user_input = int(input(f"Enter the elements in list {i+1}: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Assining an empty list
# Populating cube of the elements in list by iterating through all elements

cube_list = []
for element in user_list:
    cube_list.append(element * element * element)
print(f"Cube of the list is: {cube_list}")