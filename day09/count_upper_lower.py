#  Count uppercase
#  Count lowercase
#  Concept : strings, .upper() & .lower()

user_input = input("Enter the sentence: ")

# assigning aggregator variables

upper_count = 0
lower_count = 0

# upper case and lower case count

for char in user_input:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print(f"Total {upper_count} characters are upper case and {lower_count} are lower case.")