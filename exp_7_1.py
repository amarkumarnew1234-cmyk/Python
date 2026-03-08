'''1. Add few names, one name in each row, in “name.txt file”. 
a. Count no of names 
b. Count all names starting with vowel 
c. Find longest name '''
try:
    n=int(input("Enter number of names to add: "))
    file=open("name.txt","w")
    for i in range(n):
        name=input("Enter name: ")
        file.write(name+"\n")
    file.close()

    file=open("name.txt","r")
    names=file.readlines()
    file.close()

    names=[x.strip() for x in names]

    total=len(names)

    vowels="AEIOUaeiou"
    vowel_count=0
    for name in names:
        if name[0] in vowels:
            vowel_count+=1

    longest=names[0]
    for name in names:
        if len(name)>len(longest):
            longest=name

    print("Total names:",total)
    print("Names starting with vowel:",vowel_count)
    print("Longest name:",longest)

except Exception as e:
    print("Error:",e)