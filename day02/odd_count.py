#counting odd numbers
#Concept: using count and loop

static_list = []

for num in range(3):
    user_input = int(input(f"Enter the list element {num+1} : "))
    static_list.append(user_input)
print(f"User list is : {static_list}")

odd_count = 0
for i in static_list:
    if i % 2 != 0:
        odd_count += 1
print(f"Total number of even numbers in the list are: {odd_count}")
