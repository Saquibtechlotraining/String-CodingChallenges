'''# Write a Python program to calculate the length of a string.
string = input("Enter the string:")
print(len(string))
'''
'''
#  Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'

string = "google.com"
from collections import Counter
result = Counter(string)
print(result)'''

'''
# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
If the string length is less than 2, return the empty string instead. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String

string = "w3resource"
first = string[0:2]
second = string[-2:]
result = first + second
if len(result) < 2:
    print("")
else:
    print(result)'''

'''
# Write a Python program to get a string from a given string where all occurrences of
# its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'

string = "restart"
var = string.rfind(string[0])
#print(var)
initial_result = string[var]
#print(inital_result)
semi_result = string.capitalize()
#print(semi_result)
final_result = semi_result.replace(initial_result, "$", 1)
result = final_result.lower()
print(result)

Not fully optimized Code'''

'''
# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string:-

string_1 = "abc"
string_2 = "xyz"

string1 = string_1.replace(string_1[0:2], string_2[0:2])
#print(string1)

string2 = string_2.replace(string_2[0:2], string_1[0:2])
#print(string2)

result = string1+ " " +string2   # adding space between two string (i.e, string1 and string2)
print(result)'''

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged. Go to the editor
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

string = "abc"
if  not string.endswith("ing"):
    var = string.split()
    var.append("ing")
    semi_result = "".join(var)
    print(semi_result)
if string.endswith("ing"):
    var = string.replace("ing", "ly")
    print(var)
