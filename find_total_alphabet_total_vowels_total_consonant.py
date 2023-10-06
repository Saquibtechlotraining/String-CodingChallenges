# Take a String from user consisting only alphabets and spaces,
# and count How many Consonants and Vowels are in the string.
# input string : 'This is example'
# Output :
# Total Alphabets : 13
# Total Vowels : 5
# Total Consonants : 8


sentence = "ThIs is example"
alphabets = sentence.replace(" ", "").lower()

print("Total alphabets in a string:", len(alphabets))

total_consonant = alphabets.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
print("Total number of consonant in a string:", len(total_consonant))

total_vowels = len(alphabets) - len(total_consonant)
print("Total number of vowels in a string:", total_vowels)
