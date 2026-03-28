# Remove digits form string
# Concept: strings and .isdigit()

user_input = input("Enter the sentence: ")

if not user_input:
    print("There is no string to check.")

else:
    count = 0
    digit_list = []
    found = False
    for char in user_input:
        if char.isdigit():
            count += 1
            digit_list.append(char)
            found = True
    print(f"Total number of digits: {count}")

    if found:
        print(f"Found digits are: {' '.join(digit_list)}")
    else:
        print("No digits in string.")