# Split into chunks
# Concept : list slicing and loops

list_size = int(input("Enter the list size: "))
step_size = int(input("Enter the step/chunk size: "))
if list_size <= 0:
    print("List is empty. Please enter correct list size")
else:    
    num_list = []
    for i in range(list_size):
        user_input = int(input(f"Enter the {i+1} element: "))
        num_list.append(user_input)
    print(f"Entered list: {num_list}")

    chunk_count = 1
    for num in range(0, list_size, step_size):
        chunk = num_list[num:num+step_size]
        print(f"Chunk {chunk_count}: {chunk}")
        chunk_count += 1