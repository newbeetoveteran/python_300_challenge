# Find average of the list elements
# Concept : using accumulator variables loops

# Taking user input to populate list

user_list = []
for i in range(4):
    user_input = int(input(f"Enter the elements in list {i+1}: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Assigning variable for sum of elements and total number of elements

count = 0
sum_num = 0
for element in user_list:
    sum_num += element
    count += 1

# Assigning variable average outside of the loop
# Avoiding floor division i.e using / instead of //

average = sum_num / count

# Printing values

print(f"Sum of elements : {sum_num}")
print(f"Total number of elements in the list: {count}")
print(f"Average of the elements in the list: {average}")