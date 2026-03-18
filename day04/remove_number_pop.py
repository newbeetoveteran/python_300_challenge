#  Remove element by index
# Concept : using pop function

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

# Index handling of the user input, edge case

target_pop = int(input("Enter the index to remove form list within list length (length - 1): "))
if -list_len <= target_pop < list_len:
    popped_num = user_list.pop(target_pop)
    print(f"List after removing the target num: {user_list}")
    print(f"Removed number form list: {popped_num}")
else:
    print("Entered index is invalid. Please enter the index within valid index of 0-3.")