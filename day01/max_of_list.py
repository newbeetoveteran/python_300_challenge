#Find maximum number in a list
#Concept: using max() function

data_list = []

for num in range(3):
    user_input = int(input(f"Enter list elements {num+1}: "))
    data_list.append(user_input)

for digit in data_list:
    maximum = max(data_list) 
print(f"Max of list is: {maximum}")