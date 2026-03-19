#  Find all duplicates
#  Concept: loops,lists

# Letting users decide the list size

list_size = int(input("Enter how many elements in list: "))

# Taking user input for elements and appending it in the list

user_list = []
for i in range(list_size):
    user_input = int(input(f"Enter element {i+1} for the list: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Aggregator list to collect duplicate and seen numbers

duplicate_list = []
seen_list = []

for num in user_list:
    if num in seen_list and num not in duplicate_list:
        duplicate_list.append(num)
    else:
        seen_list.append(num)
print(f"Duplicate numbers in list are: {duplicate_list}")