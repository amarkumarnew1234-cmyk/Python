'''8. Write a program to check whether all the values in a dictionary are same or not using 
lambda function. '''
check_same=lambda d: len(set(d.values()))==1

data={}
n=int(input("Enter number of key-value pairs: "))
for i in range(n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    data[key]=value

if check_same(data):
    print("All values are same")
else:
    print("Values are not same")