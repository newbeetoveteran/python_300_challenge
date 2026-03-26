# Find missing number
# Concept : list and maths

num_list = [1,2,3,4,6]
list_len = len(num_list) + 1
expected_sum = list_len * (list_len + 1) // 2
original_sum = sum(num_list)

if expected_sum == original_sum:
    print("No number missing")

else:
    print(f"Missing number is {expected_sum - original_sum}")