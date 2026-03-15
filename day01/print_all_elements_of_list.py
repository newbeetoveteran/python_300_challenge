# Print all elements of a list
# Concept : list, inout from user and loop

user_entered_list = []

for i in range (4):
    user_input_list = int(input(f"Enter list element {i+1}: "))
    user_entered_list.append(user_input_list)
print(f"User entered elements of the list are: {user_entered_list}")