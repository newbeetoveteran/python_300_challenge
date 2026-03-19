#  Find index of largest
#  Concept: Using max(), loop and enumerate()

user_list = []
for i in range(4):
    user_input = int(input(f"Enter element {i+1} for list 1: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Finding max() 

max_list = max(user_list)

# Enumerating the user list and finding index of the variable num
# enumerate() is used when index and variable value are required at the same time
# Gives first max() index in a list with repeating max element

for index, num in enumerate(user_list):
    if num == max_list:
        break
print(f"Index of largest number in the list is: {index}")