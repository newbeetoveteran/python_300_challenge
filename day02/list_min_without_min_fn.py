#Finding minimum in a list
#Concept: using 

static_list = []

for num in range(3):
    user_input = int(input(f"Enter the list element {num+1} : "))
    static_list.append(user_input)

for digit in static_list:
    minimum = static_list[0]
    if digit < minimum:
        minimum = digit
print(f"Minimum of the list is: {minimum}")