# Most frequent character
# Concept: using loops, sets and max(dictionary, key = dictionary.get)

user_input = " "

while not user_input.strip():
    user_input = input("Enter the string: ")
    if not user_input.strip():
        print("Are you sure you entered something? Wanna try again?")

most_frequent_char = {}

for char in user_input:
    if char in most_frequent_char:
        most_frequent_char[char] += 1
    else:
        most_frequent_char[char] = 1
max_char = max(most_frequent_char, key = most_frequent_char.get)
print(f"Most frequent char is: {max_char} (count: {most_frequent_char[max_char]})")
