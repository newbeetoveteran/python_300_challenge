#find length of the list
#Concept: using loop to find length of the list from user input list

user_input_list = []

for num in range(4):
    user_input = int(input(f"Enter elements of the list(non-negative) {num+1}: "))
    user_input_list.append(user_input)
print(f"Entered list is : {user_input_list}")

count = 0
for digit in user_input_list:
    count += 1
print(f"Length of the user entered list is : {count}")