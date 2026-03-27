#  Count words
#  Concept: strings and .split()

user_input = input("Enter the string/sentence: ")

for char in user_input:
    words = user_input.split()
    word_count = len(words)
print(f"Total number of words in the sentence is: {word_count}")