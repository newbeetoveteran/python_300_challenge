#Find difference between max and min



original_list = []

for num in range(5):
    user_input = int(input(f"Enter the list element {num+1} : "))
    original_list.append(user_input)
print(f"User list is : {original_list}")

max_list = original_list[0]
min_list = original_list[1]
for i in original_list:
    if i > max_list:
        max_list = i
print(f"Max of the list is: {max_list}")

for digit in original_list:
    if digit < min_list:
        min_list = digit
print(f"Min of the list is: {min_list}")
difference = print(f"Difference of Max and Min is : {max_list-min_list}")