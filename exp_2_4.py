'''
4. Find the greatest among three numbers assuming no two values are same.  
'''
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is greatest among three numbers")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greatest among three numbers")
else:
    print(f"{num3} is greatest among three numbers")