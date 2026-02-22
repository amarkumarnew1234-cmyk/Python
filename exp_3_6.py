'''6. Write a program to print sum of digits. '''
n=int(input("Enter number:"))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("Sum of digits:",sum)

