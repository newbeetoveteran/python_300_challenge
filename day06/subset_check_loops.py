#  Subset check
#  Concept: list conversion to set. Using loop


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

    subset = True
    for item in list1:
        if item not in list2:
            subset = False
            break
    
    if subset:
        print(f"{list1} is subset of {list2}.")

    else:
        print(f"{list1} is not a subset of {list2}")   