#Find second largest number
#Concept : list, loop and nested loop

original_list = []

for num in range(5):
    user_input = int(input(f"Enter the list element {num+1} : "))
    original_list.append(user_input)
print(f"User list is : {original_list}")

largest_num = original_list[0]
second_largest_num  = original_list[1]

for digit in original_list:
    if digit > largest_num:
        second_largest_num = largest_num
        largest_num = digit
    elif digit > second_largest_num and digit != largest_num:
        second_largest_num = digit
print(f"Second largest number in the list is : {second_largest_num}")