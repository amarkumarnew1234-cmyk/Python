'''5. Given a string containing both upper and lower case alphabets. Write a Python program 
to count the number of occurrences of each alphabet (case insensitive) and display the 
same. 
Sample Input 
ABaBCbGc 
Sample Output 
2A 
3B 
2C 
1G'''
s = input("Enter string: ")
count = {}
for char in s:
    if char.isalpha():
        key = char.upper()
        if key in count:
            count[key] += 1
        else:
            count[key] = 1
for key in sorted(count):
    print(f"{count[key]}{key}")
