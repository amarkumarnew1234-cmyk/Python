'''
8. Write a program to swap two numbers without taking additional variable. 
'''
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("First number:", a)
print("Second number:", b)