#Remove duplicate
#concept: 

original_list = []

for num in range(5):
    user_input = int(input(f"Enter the list element {num+1} : "))
    original_list.append(user_input)
print(f"User list is : {original_list}")


filtered_list = []
for i in original_list:
    if i not in filtered_list:
        filtered_list.append(i)
print(f"List after removing duplicate elements: {filtered_list}")
