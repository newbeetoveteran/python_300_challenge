#Find difference between max and min
#Concept : using max and min fn to find max and min and printing the difference

# Taking user input
original_list = []

for num in range(5):
    user_input = int(input(f"Enter the list element {num+1} : "))
    original_list.append(user_input)
print(f"User list is : {original_list}")

# Max and Min of list

max_list = max(original_list)
min_list = min(original_list)

# Printing Max and Min of the list

print(f"Max of the list is: {max_list}")
print(f"Min of the list is: {min_list}")

# Printing difference of Max & Min

print(f"Difference of Max and Min in the list is : {max_list-min_list}")