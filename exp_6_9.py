'''9. Write a program to create two lists and generate a dictionary with keys from list1 and 
values from list2. '''
n=int(input("Enter number of elements: "))

list1=[]
list2=[]

print("Enter elements of list1:")
for i in range(n):
    list1.append(input())

print("Enter elements of list2:")
for i in range(n):
    list2.append(input())

result=dict(zip(list1,list2))

print("Generated Dictionary:",result)