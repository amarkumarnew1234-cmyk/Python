'''
6. Write a program to find area of triangle when length of sides are given.
'''
a = float(input("Enter the 1st side: "))
b = float(input("Enter the 2nd side: "))
c = float(input("Enter the 3rd side: "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of the triangle is:", area)