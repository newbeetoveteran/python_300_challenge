#  Rotate list left by k
#  Concept: Using pop() & loop 

user_list = []
for i in range(4):
    user_input = int(input(f"Enter element {i+1} for list 1: "))
    user_list.append(user_input)
print(f"User entered: {user_list}")

# Taking value of k from user i.e how many positions user wants to rotate left
# Remember if k is more than list length, its basically k % list_len

k = int(input("Enter no of positions you want to rotate left: "))

for _ in range(k):
    first_num = user_list.pop(0)
    user_list.append(first_num)

print(f"Rotated list by k: {user_list}")