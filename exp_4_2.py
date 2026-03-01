'''2.  Count total number of vowels in a given string. '''
string=input("Enter the string:")
vowel_count=0
for char in string:
    if char.lower() in "aeiou":
        vowel_count+=1
print("Number of vowels:",vowel_count)
