# find running sum
# Concept: using list and loops


list_size = int(input("Enter the list size: "))

static_list = []
for num in range(list_size):
    user_input = int(input(f"Enter element {num +1} element of the list: "))
    static_list.append(user_input)
print(f"You entered: {static_list}")

previous_num = 0
running_sum_list = []
for digit in static_list:
    previous_num += digit
    running_sum_list.append(previous_num)
print(f"Total sum of {static_list} list is {previous_num} and runnung sum list is: {running_sum_list}")