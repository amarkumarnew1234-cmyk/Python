'''
10. Write a program to print the following pattern 
123454321 
1234 *4321 
123  * * 321 
12   * * *  21 
1    * * * *   1 
'''
n=5
for i in range(n):
    for j in range(1,n-i):
        print(j,end="")
    if i==0:
        print(n,end="")
    else:
        print(" ",end="")
        for k in range(i):
            print("* ",end="")
    for j in range(n-i-1,0,-1):
        print(j,end="")
    print()
