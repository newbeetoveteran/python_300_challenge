#  Rotate list right by 1
#  Concept: Using pop() & loop 

user_list = []
for i in range(4):
    user_input = int(input(f"Enter element {i+1} for list 1: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Popping last element and appending it in the list in front
# inserting last number in front

last_num = user_list.pop(len(user_list) - 1)
user_list.insert(0, last_num)

print(f"Right rotated by 1: {user_list}")
