'''6. Write a program to create a counter to show that how many times the program is executed.'''
try:
    file=open("counter.txt","r")
    count=int(file.read())
    file.close()
except:
    count=0

count+=1
file=open("counter.txt","w")
file.write(str(count))
file.close()

print("Program executed",count,"times")