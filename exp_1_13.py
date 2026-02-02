'''
11. Write a program to find left shift and right shift values of a given number. 
'''
num = int(input("Enter a number: "))
left_shift = num << 1
right_shift = num >> 1
print("Left shift of", num, "is:", left_shift)
print("Right shift of", num, "is:", right_shift)