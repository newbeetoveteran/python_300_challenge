# Find common elements in list
# Concept : using loop

user_list1 = []
for i in range(4):
    user_input1 = int(input(f"Enter element {i+1} for list 1: "))
    user_list1.append(user_input1)
print(f"User entered: {user_list1}")

# Taking user input for list 2

user_list2 = []
for i in range(3):
    user_input2 = int(input(f"Enter element {i+1} for list 2: "))
    user_list2.append(user_input2)
print(f"User entered: {user_list2}")

common_num_list = []

for num in user_list1:
    if num in user_list2 and num not in common_num_list:
        common_num_list.append(num)
print(f"Common elements in both lists are: {common_num_list}")