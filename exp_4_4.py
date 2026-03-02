'''4. WAP to enter a string and a substring. You have to print the number of times that the 
substring occurs in the given string. String traversal will take place from left to right, not 
from right to left. 
Sample Input 
ABCDCDC
CDC 
Sample Output 
2 '''
main_string=input("Enter the string:")
sub_string=input("Enter the substring:")
count=0
for i in range(len(main_string)-len(sub_string)+1):
    if main_string[i:i+len(sub_string)]==sub_string:
        count+=1
print(count)
