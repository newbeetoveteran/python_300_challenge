#Finding minimum in a list
#Concept: using for loop and user input


static_list = []

for num in range(3):
    user_input = int(input(f"Enter the list element {num+1} : "))
    static_list.append(user_input)

# finding Min of the list

minimum = min(static_list)
print(f"Min of the list is: {minimum}")