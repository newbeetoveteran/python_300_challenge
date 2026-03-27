# Replace charecters
# Concept: String and replace

user_input = input("Enter the sentence: ")
replace_char = input("Enter the charater your want to replace: ")
new_char = input("Enter the character you want to add: ")

replaced = user_input.replace(replace_char, new_char)

print(f"Sentence after replacing {replace_char} with {new_char}: {replaced}")