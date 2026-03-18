#  Separate even & odd
# Concept : Find even and odd and populate in a separate list using loop


user_list = []
for i in range(4):
    user_input = int(input(f"Enter the elements in list {i+1}: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Finding even and odd
# Allocating even_list and odd_list for num based on type by iterating through user_list

even_list = []
odd_list = []

for num in user_list:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print(f"List of even num: {even_list}")
print(f"List of odd num: {odd_list}")