# Find all duplicates
# Concept : list, loops

list_size = int(input("Enter size of the list: "))

static_list = []
if list_size == 0:
    print("List is empty. Please enter correct list size.")
else:
    for num in range(list_size):
        user_input = int(input(f"Enter the {num+1} element: "))
        static_list.append(user_input)
    print(f"You entered: {static_list}")

    duplicate_list = []
    unique_list = []
    for i in static_list:
        if i not in unique_list:
            unique_list.append(i)
        else:
            duplicate_list.append(i)
    print(f"Duplicate list: {duplicate_list}")
    print(f"Unique list: {unique_list}")