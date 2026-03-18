# Check if element exists
# Concept : Easier version code by using "in"

user_list = []
for i in range(4):
    user_input = int(input(f"Enter the elements in list {i+1}: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Assigning a variable to collect target element and initializing found as false

target_value = int(input("Enter the number you want to search: "))

if target_value in user_list:
    print(f"The list contains the number {target_value}")
else:
    print(f"The list does not contain the number {target_value}")