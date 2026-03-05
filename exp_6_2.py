'''2. Write a Python function that takes a positive integer and returns the sum of the cube of 
all the positive integers smaller than the specified number.  '''
def sum_of_cubes(n):
    if n<=0:
        return 0
    total=0
    for i in range(1,n):
        total=total+(i*i*i)
    return total
num=int(input("Enter a positive integer:"))
result=sum_of_cubes(num)
print("Sum of cubes:",result)