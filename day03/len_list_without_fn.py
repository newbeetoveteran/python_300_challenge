# Print list without using len()
# Concept : using loop to find the length of the list

# Taking user input to populate list

static_list = []

for i in range(4):
    user_input = int(input(f"Enter the list element {i+1}: "))
    static_list.append(user_input)
print(f"User entered: {static_list}")

# Assigning count variabble as 0 - starting count of elements in the list

count = 0

# Looping through each element of the static_list

for element in static_list:
    count += 1
print(f"Total number of elements in the list : {count}")