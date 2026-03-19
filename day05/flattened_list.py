# Flatten a nested list without extend
# Concept : using list and loop

nested_list = [[1,2], [3,6]]

print(f"Nested list: {nested_list}")

flattened_list = []

for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)
print(f"Flattened list is: {flattened_list}")