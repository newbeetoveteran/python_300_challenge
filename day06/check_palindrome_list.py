#  Check palindrome list
# Concept: using list

new_list = []
reverse_list = []
list_size = int(input("Enter the size of the list: "))
if list_size <= 0:
    print("List is empty. Please enter correct list size.")
    exit()
else:
    for i in range(list_size):
        user_input = int(input(f"Enter the {i+1} element: "))
        new_list.append(user_input)
    print(f"You entered: {new_list}")

    reverse_list = new_list[::-1]
    print(f"Reverse list: {reverse_list}")

    if new_list == reverse_list:
        print("Palindrome")
    else:
        print("Not palindrome")