#  Find difference
#  Concept: sets and .difference()

set_size1 = int(input("Enter size of the set1: "))
set_size2 = int(input("Enter size of the set2: "))

static_set1 = set()
static_set2 = set()

if set_size1 == 0:
    print("Set is empty. Please enter correct set size for set 1.")
else:
    for i in range(set_size1):
        user_input1 = int(input(f"Enter the {i+1} element for set 1: "))
        static_set1.add(user_input1)
    print(f"First set: {static_set1}")

if set_size2 == 0:
    print("Set is empty. Please enter correct set size for set 2.")

else:
    for j in range(set_size2):
        user_input2 = int(input(f"Enter the {j+1} element for set 2: "))
        static_set2.add(user_input2)
    print(f"Second set: {static_set2}")

difference_set = static_set1.difference(static_set2)

print(f"Difference of 2 sets: {difference_set}")