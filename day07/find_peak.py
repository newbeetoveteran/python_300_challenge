# Find peaks in list
# Concept: Using list

list_size = int(input("Enter the list size: "))

if list_size <= 0:
    print("List is empty. Please enter correct list size")
else:    
    num_list = []
    for i in range(list_size):
        user_input = int(input(f"Enter the {i+1} element: "))
        num_list.append(user_input)
    print(f"Entered list: {num_list}")

    found = False
    for num in range(1,len(num_list)-1):
        if num_list[num]> num_list[num-1] and num_list[num] > num_list[num+1]:
            print(f"Peak element is {num_list[num]}")
            found = True
    if not found:
        print("There is no Peak element")