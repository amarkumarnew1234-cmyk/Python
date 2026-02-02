'''
12. Using membership operator find whether a given number is in sequence
(10,20,56,78,89) 
'''
sequence = (10, 20, 56, 78, 89)
num = int(input("Enter a number to check: "))
if num in sequence:
    print("The number is in the sequence.")
else:
    print("The number is not in the sequence.")