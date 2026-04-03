# check anagram
# concept : check if string size is same and shuffle the words

user_input1 = " "
user_input2 = " "

while not user_input1.strip():
    user_input1 = input("Enter the first word: ")
    if not user_input1.strip():
        print("Please enter valid input.")

while not user_input2.strip():
    user_input2 = input("Enter the second word: ")
    if not user_input2.strip():
        print("Please enter valid input.")

word1 = user_input1.replace(" ", "").lower()
word2 = user_input2.replace(" ", "").lower()

if sorted(word1) == sorted(word2):
    print(f"{user_input1} and {user_input2} are Anagram!")
else:
    print(f"{user_input1} and {user_input2} are not Anagram")