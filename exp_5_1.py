''' 
1. Scan n values in range 0-3 and print the number of times each value has occurred.'''
n = int(input("Enter no. of values: "))

count = [0, 0, 0, 0]

print("Enter values (0-3):")
for i in range(n):
    value = int(input())
    if 0 <= value <= 3:
        count[value] += 1
    else:
        print("Invalid input, ignored")

print("Count of 0:", count[0])
print("Count of 1:", count[1])
print("Count of 2:", count[2])
print("Count of 3:", count[3])