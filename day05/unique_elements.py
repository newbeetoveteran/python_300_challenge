# Find unique elements
# Concept : Using not in and loop

user_list = []
for i in range(4):
    user_input = int(input(f"Enter element {i+1} for the list: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

unique_list = []

for num in user_list:
    if num not in unique_list:
        unique_list.append(num)
print(f"Unique elements in the list: {unique_list}")