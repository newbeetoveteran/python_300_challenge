# Shift zeros to end


list_size = int(input("Enter the size of list : "))

list1 = []

if list_size <= 0:
    print(f"List is empty. Please enter correct list size.")
else:
    for i in range(list_size):
        user_input = int(input(f"Enter {i+1} element: "))
        list1.append(user_input)
    print(f"Entered list : {list1}")

    zero_list = []
    non_zero_list = []
    for num in range(list_size):
        if list1[num] == 0:
            zero_list.append(num)
        else:
            non_zero_list.append(num)
    sorted_list =  sum(non_zero_list, zero_list)
    print(f"{sorted_list}")