# Find mode of a list
# Concept: list and loop

list_size = int(input("Enter size of the list: "))

static_list = []
if list_size == 0:
    print("List is empty. Please enter correct list size.")
else:
    for num in range(list_size):
        user_input = int(input(f"Enter the {num+1} element: "))
        static_list.append(user_input)
    print(f"You entered: {static_list}")


    highest_count = 0
    mode = None

    for i in static_list:
        count = 0
        for j in static_list:
            if i == j:
                count += 1
        print(f"{i} appeared {count} times.")
        if count > highest_count:
            highest_count = count
            mode = i
    print(f"Mode of the list is: {mode}")