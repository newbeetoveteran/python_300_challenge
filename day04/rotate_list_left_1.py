#  Rotate list left by 1
#  Concept: Using pop() & loop 

user_list = []
for i in range(4):
    user_input = int(input(f"Enter element {i+1} for list 1: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Popping first element and appending it in the list later at last

first_num = user_list.pop(0)
user_list.append(first_num)

print(f"Rotated list by 1: {user_list}")