# Find repeating number
# Concept : list and loop

list_size = int(input("Enter the list size: "))

if list_size <= 0:
    print("List is empty. Please enter valid list size.")
else:
    user_list = []
    for i in range(list_size):
        user_input = int(input(f"Enter the {i+1} element: "))
        user_list.append(user_input)
    print(f"You entered: {user_list}")

    repeating_num = []
    unique = []
    for num in user_list:
        if num not in unique:
            unique.append(num)
        else:
            if num not in repeating_num:
               repeating_num.append(num)
    print(f"Repeating numbers in list: {repeating_num}")