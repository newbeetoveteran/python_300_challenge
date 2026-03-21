# Finding median of the list
# Concept : using sort() function, list and loop


list_size = int(input("Enter the list size: "))
if list_size == 0:
    print("List is empty. Median can not be defined")
    exit()
else:
    static_list = []
    for num in range(list_size):
        user_input = int(input(f"Enter element {num +1} element of the list: "))
        static_list.append(user_input)
    print(f"You entered: {static_list}")

    static_list.sort()  # sort list first for finding the median
    print(f"Sorted list: {static_list}")

    if list_size % 2 != 0:
        median = static_list[list_size // 2]
    else:
        median = (static_list[list_size // 2 -1] + static_list[list_size // 2]) / 2  # finding left median and right median

    print(f"Median of the list is: {median}")