# You are tasked to swap first and last characters of a string.
# For Example:
# Input string : 'python'
# Output : 'nythop'

string = "python"
print("String whose first and last character has to be swap:",string)
first_character = string[0]                             # p
last_character = string[-1]                             # n
var = string.replace(first_character, last_character)   # nython
#print(var)
kt = var.title()                                        # Nython
#print(kt)

rt = kt.replace(last_character, first_character)        # Nythop
#print(rt)
result = rt.lower()                                     # nythop
print("String after swap the first and last character:", result)