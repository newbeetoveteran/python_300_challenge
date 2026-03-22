#  Find pair with max product
#  Concept : using list, loop and manual max finding

list_size = int(input("Enter size of the list: "))
target_num = int(input("Enter the target num: "))

static_list = []
if list_size == 0:
    print("List is empty. Please enter correct list size.")
else:
    for num in range(list_size):
        user_input = int(input(f"Enter the {num+1} element: "))
        static_list.append(user_input)
    print(f"You entered: {static_list}")

    target_element = []
    num_found = False
    for i in range(list_size):
        for j in range(i+1, list_size):
            if static_list[i] * static_list[j] == target_num:
                target_element.append((static_list[i], static_list[j]))
                print(f"Found")
                num_found = True
    if not num_found:
        print("Pair not found")
    else:
        print(f"All pairs with product {target_num}: {target_element}")