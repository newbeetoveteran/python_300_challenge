# Find missing number in series
# Concept: List and loop

num_list = [1,2,3,5,6]

list_range = len(num_list)+1
for num in range(1, list_range+1):
    if num not in num_list:
        print(f"Missing number: {num}")