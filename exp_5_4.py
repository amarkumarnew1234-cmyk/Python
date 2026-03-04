'''4. Create a dictionary of n persons where key is name and value is city.  
a) Display all names 
b) Display all city names 
c) Display student name and city of all students. 
d) Count number of students in each city. '''
n = int(input("Enter no. of persons: "))

d = {}

print("Enter name and city:")
for i in range(n):
    name = input("Name: ")
    city = input("City: ")
    d[name] = city

print("\nAll Names:")
for name in d.keys():
    print(name)

print("\nAll Cities:")
for city in d.values():
    print(city)

print("\nStudent Name and City:")
for name, city in d.items():
    print(name, "->", city)

print("\nNumber of students in each city:")
city_count = {}

for city in d.values():
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

for city, count in city_count.items():
    print(city, ":", count)