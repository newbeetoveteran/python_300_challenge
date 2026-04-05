# #  Swap first & last char
#  concept : slicing and loop - swapping first and last of each word

user_input = " "

while not user_input.strip():
    user_input = input("Enter the string: ")
    if not user_input.strip():
        print("No valid input found. Please try again.")

words = user_input.split()
word_list = []

for char in words:
    if len(char) > 1:
        swapped = char[-1] + char[1:-1] + char[0]
    else:
        swapped = char
    word_list.append(swapped)
output = " ".join(word_list)
print(f"Final output after swapping each word: {output}")
