'''4. Write a recursive function to print Fibonacci series upto n terms.'''
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
def print_fibonacci(n):
    if n<=0:
        return
    print_fibonacci(n-1)
    print(fibonacci(n-1),end=" ")
n=int(input("Enter no. of terms:"))
print_fibonacci(n)