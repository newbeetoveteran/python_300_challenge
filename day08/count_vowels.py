#  Count vowels
#  Concept: string

user_input = input("Enter the sentence: ")
vowels = "aeiouAEIOU"

vowel_count = 0

for char in user_input:
    if char in vowels:
        vowel_count += 1
print(f"Total vowels in your sentence are: {vowel_count}")