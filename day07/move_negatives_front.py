# Move negatives to front
#Concept : lists and loop

list_size = int(input("Enter the size of list : "))

list1 = []

for i in range(list_size):
    user_input = int(input(f"Enter {i+1} element: "))
    list1.append(user_input)
print(f"Entered list : {list1}")

negative_list = []
non_negative_list = []
for num in list1:
    if num < 0:
        negative_list.append(num)
    else:
        non_negative_list.append(num)
sorted_list = negative_list + non_negative_list

print(f"Sorted list with negative numbers in fron: {sorted_list}")