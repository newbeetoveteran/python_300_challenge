# Check if element exists
# Concept : using list, loop and user input using break and initializing boolean

user_list = []
for i in range(4):
    user_input = int(input(f"Enter the elements in list {i+1}: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Assigning a variable to collect target element and initializing found as false

target_value = int(input("Enter the number you want to search: "))
found = False

# Iterating through the list

for num in user_list:
    if num == target_value:
        found = True
        break
if found:
    print(f"{user_list} contains the {target_value}")
else:
    print(f"The list does not contain the {target_value}")
