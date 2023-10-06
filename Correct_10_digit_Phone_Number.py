# You work in a company and you are given customers number,
# But many customers filled wrong data, so you need to check if the number given by customer is right or not.
# Phone Number should match following Criteria :
# Only numbers , spaces are allowed though (so few customers wrote their number with spaces.)
# 10 digits only.

string = input("Enter the number:")
check_number = string.replace(" ", "")
if check_number.isnumeric() and len(check_number) == 10:
    print("check_number:","True", "and", "ten digit:","True")

else:
    print("Not valid number")

