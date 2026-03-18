#  Remove element by index
# Concept : using del

# Taking user input

user_list = []
for i in range(4):
    user_input = int(input(f"Enter element {i+1} for list 1: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Taking user input index
# Letting user know len of list

list_len = len(user_list)
print(f"Length of the list is: {list_len}")

# Taking index input from user to remove

target_num = int(input("Enter the index to remove form list within list length: "))

# Handling edge case/ index handling

if -list_len <= target_num < list_len:
    removed = user_list[target_num]
    del(user_list[target_num])
    print(f"List after removing the element: {user_list}")
    print(f"Removed element: {removed}")
else:
    print("Entered number is not a valid index. Please enter correct index within range.")