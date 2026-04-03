# sort words in string
# concept: using .split(), .join() and sorted()

user_input = " "

while not user_input.strip():
    user_input = input("Enter the string: ")
    if not user_input.strip():
        print("No valid input found. Try again.")

sorted_words_string = " ".join(sorted(user_input.split()))
print(f"After sorting words in string: {sorted_words_string}")