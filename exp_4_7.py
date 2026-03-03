'''7. Create 2 sets s1 and s2 of n fruits each by taking input from user and find: 
a) Fruits which are in both sets s1 and s2 
b) Fruits only in s1 but not in s2 
c) Count of all fruits from s1 and s2 '''
n=int(input("Enter number of fruits in each set:"))
s1=set()
s2=set()
print("Enter fruits for set 1:")
for i in range(n):
    fruit=input()
    s1.add(fruit.lower())
print("Enter fruits for set 2:")
for i in range(n):
    fruit=input()
    s2.add(fruit.lower())
common_fruits=s1&s2
only_s1=s1-s2
all_fruits=s1|s2
print("Fruits in both sets:",common_fruits)
print("Fruits only in s1:",only_s1)
print("Count of all fruits:",len(all_fruits))
