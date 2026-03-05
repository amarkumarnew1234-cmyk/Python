'''1. Write a Python function to find the maximum and minimum numbers from a sequence of 
numbers.  (Note: Do not use built-in functions.) '''
def find_max_min(numbers):
    if len(numbers)==0:
        return None
    maximum=numbers[0]
    minimum=numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i]>maximum:
            maximum=numbers[i]
        if numbers[i]<minimum:
            minimum=numbers[i]
    return maximum,minimum
n=int(input("Enter no. of elements:"))
numbers=[]
for i in range(n):
    value=int(input())
    numbers.append(value)
result=find_max_min(numbers)
if result is None:
    print("No elements in sequence")
else:
    print("Maximum:",result[0])
    print("Minimum:",result[1])