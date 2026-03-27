#  Find longest word
# Concept: string, split()

user_input = input("Enter the sentence: ")

word_len = 0
largest_word_list = []
# spliting sentence into words

words = user_input.split()

# looping through each word

for word in words:
    if len(word) > word_len:
        word_len = len(word)
        largest_word_list = [word]
    elif len(word) == word_len:
        largest_word_list.append(word)
print(f"Largest words: {largest_word_list} with {word_len} charaters.")
