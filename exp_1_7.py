'''
5. Write a program to find simple interest. 
'''
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)