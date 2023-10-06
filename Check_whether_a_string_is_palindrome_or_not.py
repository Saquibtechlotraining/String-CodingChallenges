# Check if a string is palindrome or not. Palindrome is a string that does not change even if you reverse it.
# For example:
# input string : 'rotator'
# Output:
# Palindrome : True
# input string : 'python'
# Output:
# Palindrome : False

string = input("Enter the word")
string_reversed = string[::-1]
if string == string_reversed:
    print("Palindrome")
else:
    print("Not palindrome")