#  Find pair with given sum
#  Concept : using list and loop

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

    found_num = False
    target_elements = []
    for i in range(len(static_list)):
        for j in range(i+1, len(static_list)):
            if static_list[i] + static_list[j] == target_num:
                target_elements.append((static_list[i], static_list[j]))
                print(f"Pair found! {target_elements}")
                found_num = True
    if not found_num:
        print("Pair not found")