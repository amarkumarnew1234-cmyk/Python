'''2. Create a tuple to store n numeric values and find average of all values.'''
n = int(input("Enter no. of values: "))

values = []

print("Enter numeric values:")
for i in range(n):
    num = float(input())
    values.append(num)

t = tuple(values)

average = sum(t) / len(t)

print("Tuple:", t)
print("Average:", average)