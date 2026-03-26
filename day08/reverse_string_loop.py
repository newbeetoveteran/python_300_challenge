# reverse string
# concept: reversing string using loop

string_1 = "This is a string"
reversed_string = ""

for char in string_1:

    # using char in front of reversed string to rather than reversed string + char
    
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")