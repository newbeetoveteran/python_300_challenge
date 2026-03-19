#  Rotate list right by k
#  Concept: Using pop(), loop and insert 

user_list = []
for i in range(4):
    user_input = int(input(f"Enter element {i+1} for list 1: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Taking user input for k

k = int(input("Enter the index by which you want to rotate right: "))

# Popping last element and appending it in the list in front
# inserting last number in front
for _ in range(k):
    last_num = user_list.pop(-1)
    user_list.insert(0, last_num)
print(f"Right rotated by {k}: {user_list}")