#sum of all numbers

static_list = []

for num in range(3):
    user_input = int(input(f"Enter the list element {num+1} : "))
    static_list.append(user_input)

sum_of_num = 0
for i in static_list:
    sum_of_num += i
print(f"Sum of all numbers : {sum_of_num}")