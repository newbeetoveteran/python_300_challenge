# Merge two lists
# Concept : using adding lists

user_list1 = []
for i in range(4):
    user_input1 = int(input(f"Enter the elements in list {i+1}: "))
    user_list1.append(user_input1)
print(f"User entered: {user_list1}")

# Taking user input for list 2

user_list2 = []
for i in range(3):
    user_input2 = int(input(f"Enter the elements in list {i+1}: "))
    user_list2.append(user_input2)
print(f"User entered: {user_list2}")

merged = user_list1 + user_list2

print(f"Merged list: {merged}")