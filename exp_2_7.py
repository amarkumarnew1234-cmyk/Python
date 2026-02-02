'''
7. Write a program which takes any date as input and display next date of the calendar 
e.g. 
I/P: day=20 month=9 year=2005  
O/P: day=21 month=9 year 2005
'''
day=int(input("Enter day no.:"))
month=int(input("Enter month no.:"))
year=int(input("Enter year:"))
if month==2:
    if (year%400==0) or (year%4==0 and year%100!=0):
        days=29
    else:
        days=28
elif month in (4,6,9,11):
    days=30
else:
    days=31
    day+=1
    if day>days:
        day=1
    month+=1
    if month>12:
        month=1
        year+=1
        print("Next date:day=",day,"month=",month,"year=",year)
