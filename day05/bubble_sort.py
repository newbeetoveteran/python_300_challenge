#  Implement bubble sort
# Concept: list and loop


# Edge case for checking empty list

list_size = int(input("Enter size of the list: "))

static_list = []
if list_size == 0:
    print("List is empty. Please enter correct list size.")
else:
    for num in range(list_size):
        user_input = int(input(f"Enter the {num+1} element: "))
        static_list.append(user_input)
    print(f"You entered: {static_list}")

# Using nested for loop to perform bubble sort
# First loop checks the len and index
# Second for loop checks if element at a given index is larger than the next element 

    for i in range(list_size):
        for j in range(list_size - i - 1):                           # list_size - 1 because index start at 0
            if static_list[j] > static_list[j+1]:
                temp = static_list[j]
                static_list[j], static_list[j+1] = static_list[j+1], static_list[j]
    print(f"Bubble sort of the list is: {static_list}")
    