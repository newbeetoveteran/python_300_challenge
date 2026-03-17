#Reverse a list
#concept: without using reversed() function


static_list = []

for num in range(3):
    user_input = int(input(f"Enter the list element {num+1} : "))
    static_list.append(user_input)
print(f"User list is : {static_list}")


for i in static_list:
    reverse_list = static_list[::-1]
print(f"Reverse of the list is: {reverse_list}")
