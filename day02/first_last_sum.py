# Find sum of first & last
# Concept : list and loops. Taking user input. List index

user_list = []
for i in range(4):
    user_input = int(input(f"Enter the elements in list {i+1}: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Allocating variables for first and last using list index as reference

first_num = user_list[0]
last_num = user_list[-1]
total = first_num + last_num
print(f"Sum of first and last num: {total}")