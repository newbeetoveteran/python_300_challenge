# Count digits
# Concept : using loop, append and .join()

user_input = input("Enter the sentence: ")

digit_count = 0
digits = []

if not user_input:
    print("No user input.")

else:
    for char in user_input:
        if char.isdigit():
            digit_count += 1
            digits.append(char)
    print(f"Total digits: {digit_count}")
    print(f"Digits: {' '.join(digits)}")