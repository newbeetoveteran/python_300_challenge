#  Multiply all elements
# Concept: Using a loop to traverse a list and calculate the product of all elements using an accumulator variable.


user_list = []
for i in range(4):
    user_input = int(input(f"Enter the elements in list {i+1}: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# looping through all elements in user_list
# assigning a variable for product. Setting it to 1 instead of 0 (as 0*num = 0) 

list_product = 1
for element in user_list:
    list_product *= element
print(f"Product of elements of the list is : {list_product}")