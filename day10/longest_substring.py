#  Longest unique substring
#  Concept: using .count() and edge case handling.

user_input = " "

while not user_input.strip():
    user_input = input("Enter the string to check: ")
    if not user_input.strip():
        print("No valid input found. Try again.")

longest_substring = ""
current_substring = ""

for char in user_input:
    if char not in current_substring:
        current_substring += char
    else:
        while char in current_substring:
            current_substring = current_substring[1:]
        current_substring += char

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

print(f"Longest unique substring: {longest_substring}")