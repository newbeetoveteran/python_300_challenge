# Check equal list
# Concept: lists and loop

list_size1 = int(input("Enter the size of list 1: "))
list_size2 = int(input("Enter the size of list 2: "))

list1 = []
list2 = []

if list_size1 <= 0 or list_size2 <= 0:
    print(f"List is empty. Please enter correct list size.")
else:
    for i in range(list_size1):
        user_input1 = int(input(f"Enter {i+1} element: "))
        list1.append(user_input1)
    print(f"Entered list 1: {list1}")
    
    for j in range(list_size2):
        user_input2 = int(input(f"Enter {j+1} element: "))
        list2.append(user_input2)
    print(f"Entered list 2: {list2}")

    if list1 == list2:
        print("Both lists are equal.")
    else:
        print("Entered list are different.")