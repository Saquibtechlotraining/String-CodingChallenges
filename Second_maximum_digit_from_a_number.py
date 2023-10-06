# Find the second maximum digit from a number.
# For Example :
# input : 494948493
# Output :
# second_maxdigit : 8

input = "494948493"
max_1 = max(input)
var = input.replace(max_1, "")
result = max(var)
print(result)
