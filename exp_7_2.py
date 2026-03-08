'''2. Store integers in a file. 
a. Find the max number 
b. Find average of all numbers 
c. Count number of numbers greater than 100 '''
try:
    n=int(input("Enter no.of integers: "))
    nums=list(map(int,input("Enter numbers: ").split()))
    if len(nums)!=n:
        raise ValueError("Count mismatch")
    file=open("numbers.txt","w")
    for num in nums:
        file.write(str(num)+"\n")
    file.close()
    file=open("numbers.txt","r")
    numbers=[int(x.strip()) for x in file.readlines()]
    file.close()
    maximum=numbers[0]
    total=0
    count_greater=0
    for num in numbers:
        if num>maximum:
            maximum=num
        total+=num
        if num>100:
            count_greater+=1
    average=total/len(numbers)
    print("Maximum number:",maximum)
    print("Average:",average)
    print("Numbers greater than 100:",count_greater)
except Exception as e:
    print("Error:",e)