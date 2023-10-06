# What is the Positive and negative index number of space in Word - David Joseph ?
# word =         "David Joseph"
# +ve indexing =  012345

# word =          "David Joseph"
# -ve indexing =       -7-6-5-4-3-2-1

# For +ve index
word = "David Joseph"
result = word.find(" ")
print("The +ve index of space in word David Joseph:", result)


# For -ve index
word = "David Joseph"
result = word.find(" ")
answer = result - len(word)
print("The -ve index of space in word David Joseph:", answer)