#  Count positive numbers
#  Concept : using loop

static_list = []

for i in range(4):
    user_input = int(input(f"Enter the list element {i+1}: "))
    static_list.append(user_input)
print(f"User entered: {static_list}")

# assigning a count variable for positive count

count = 0

for element in static_list:
    if element > 0:
        count += 1
print(f"Total number of positive elements in the list: {count}")