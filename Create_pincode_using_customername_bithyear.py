# You work in a bank, You are tasked to create a pin with the help of their customer name  and birthyear .
#  Input Customer Name : david josh
# Indexing:              0123456789
# Input Date Of Birth : 09-12-1997
#Indexing:              0123456789
# Output:
# pin : David1997

Name = "david josh"
date = "09-12-1997"
naming = Name.capitalize()      # David josh
space_find = naming.find(" ")   # 5
#print(space_find)
date_find = date.rfind("-")     # 5
#print(date_find)
result = naming[0:space_find]   # naming[0:5] = David
result_1 = date[date_find+1:]   # date[6:] = 1997
#print(result_1)
output = result + result_1      # output = David + 1997
print("pin:",output)            # Pin: David1997