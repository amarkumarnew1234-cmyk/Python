'''1.  Write a program to count and display the number of capital letters in a given string.'''
string=input("Enter the string:")
capital_count=0
for char in string:
    if char.isupper():
        capital_count+=1
print("Capital letters:",capital_count)
