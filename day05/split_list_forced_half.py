# Spliting a list in half
# Concept : using slicing loop for user input and - for ignoring the middle element in case list has odd length


list_size = int(input("Enter the list size: "))

static_list = []
for num in range(list_size):
    user_input = int(input(f"Enter element {num +1} element of the list: "))
    static_list.append(user_input)
print(f"You entered: {static_list}")

# spliting/slicing list in mid
# using len() to determine the equal half

half_list = len(static_list) // 2
first_half = static_list[:half_list]
second_half = static_list[-half_list:]  # using[-half_list:] to ignore the middle element for equal divisio of list size

# Printing both halves

print(f"First half of the list is: {first_half}")
print(f"Second half of the list is: {second_half}")
