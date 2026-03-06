'''3. Write a Python function to print 1 to n using recursion. (Note: Do not use loop) '''
def print_numbers(n):
    if n<=0:
        return
    print_numbers(n-1)
    print(n)
n=int(input("Enter a positive integer:"))
print_numbers(n)