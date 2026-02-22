'''3. Print Fibonacci series up to given term.'''
n=int(input("Enter term:"))
a=0
b=1
if n<=0:
    print("Invalid input")
elif n==1:
    print(a)
else:
    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
