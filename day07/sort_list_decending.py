#  Sort descending
#  Concept: using list and loop


list_size = int(input("Enter the size of list : "))

list1 = []

if list_size <= 0:
    print(f"List is empty. Please enter correct list size.")
else:
    for i in range(list_size):
        user_input = int(input(f"Enter {i+1} element: "))
        list1.append(user_input)
    print(f"Entered list : {list1}")

    for num in range(list_size):
        for digit in range(list_size - num - 1):
            if list1[digit] < list1[digit + 1]:
                list1[digit], list1[digit + 1] = list1[digit + 1], list1[digit]
    print(f"Sorted list in decending order: {list1}")