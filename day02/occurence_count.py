#  Count occurrences of element
#  Concept : using list, loop and user input and without using dictionary


user_list = []
for i in range(4):
    user_input = int(input(f"Enter the elements in list {i+1}: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Making search user driven

target_num = int(input("Enter the number to find: "))

# Accumulator variable for collecting count

count = 0

# Counting occurance of 4 in the list

for num in user_list:
    if num == target_num:
        count += 1
print(f"Total count of occurence of {target_num} in the list is: {count}")
