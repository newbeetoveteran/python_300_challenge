#Find maximum number in a list
#Concept: without max function using loop

data_list = []

for num in range(3):
    user_input = int(input(f"Enter list elements {num+1}: "))
    data_list.append(user_input)

maximum = data_list[0]
for digit in data_list:
    if digit > maximum:
        maximum = digit
print(f"Max of list is : {maximum}")