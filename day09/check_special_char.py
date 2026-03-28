# Count special characters in a sentence
# Concept: Check if string contains numbers, whitespaces or digits

user_input = input("Enter the sentence for special character check: ")

if not user_input:
    print("There is no input. Please enter the sentence.")

else:

# Adding aggregator variable for total count of special characters
# Creating a list to store all special characters
    
    char_count = 0
    special_char_list = []
    for char in user_input:
        if not char.isalnum() and not char.isspace():
            char_count += 1
            special_char_list.append(char)
    print(f"Total special characters: {char_count}")
    print(f"Special characters: {" ".join(special_char_list)}")