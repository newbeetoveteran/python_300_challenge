# Flatten a nested list
# Concept : append() and loops

# creating a nested list

list_size = int(input("Enter size of the list: "))
user_list = []
for i in range(list_size):
    user_sublist = []
    sublist_size = int(input(f"Enter the size of sublist {i+1}: "))
    for j in range(sublist_size):
        user_input = int(input(f"Enter the {j+1} element: "))
        user_sublist.append(user_input)
    user_list.append(user_sublist)
print(f"Nested loop: {user_list}")