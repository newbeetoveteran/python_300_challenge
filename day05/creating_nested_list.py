# Create a nested list
# Concept : append() and loops

# taking user input for size of the list

list_size = int(input("Enter size of the list: "))
user_list = []

# looping through the main list based on user defined size

for i in range(list_size):
    user_sublist = []
    sublist_size = int(input(f"Enter the size of sublist {i+1}: "))

# looping through sublist and appending the element value

    for j in range(sublist_size):
        user_input = int(input(f"Enter the {j+1} element: "))
        user_sublist.append(user_input)
    user_list.append(user_sublist)

# Printing the final nested list

print(f"Nested loop: {user_list}")