'''
8. Print the grade sheet of a student for the given range of cgpa. Scan marks of five 
subjects and calculate the percentage. 
CGPA=percentage/10 
CGPA range: 
0 to 3.4 -> F 
3.5 to 5.0->C+ 
5.1 to 6->B 
6.1 to 7-> B+ 
7.1 to 8-> A 
8.1 to 9->A+ 
9.1 to 10-> O (Outstanding) 
Sample Gradesheet 
Name: Rohit Sharma 
Roll Number: R17234512   SAPID: 50005673 
Sem: 1      Course: B.Tech. CSE AI&ML 
 
Subject name: Marks 
PDS:   70 
Python:  80 
Chemistry:  90 
English:  60 
Physics:  50 
Percentage: 70% 
CGPA:7.0 
Grade:   
'''
name=input("Enter Name:")
roll=input("Enter Roll Number:")
sapid=input("Enter SAPID:")
sem=input("Enter Semester:")
course=input("Enter Course:")

print("Enter marks of five subjects")
pds=int(input("PDS:"))
python=int(input("Python:"))
chem=int(input("Chemistry:"))
eng=int(input("English:"))
phy=int(input("Physics:"))

total=pds+python+chem+eng+phy
percentage=total/5
cgpa=percentage/10

if cgpa<=3.4:
    grade="F"
elif cgpa<=5.0:
    grade="C+"
elif cgpa<=6.0:
    grade="B"
elif cgpa<=7.0:
    grade="B+"
elif cgpa<=8.0:
    grade="A"
elif cgpa<=9.0:
    grade="A+"
else:
    grade="O (Outstanding)"
print("\nSample Gradesheet")
print(f"Name: {name}")
print(f"Roll Number: {roll}   SAPID: {sapid}")
print(f"Sem: {sem}      Course: {course}")
print("\nSubject name: Marks")
print(f"PDS:   {pds}")
print(f"Python:  {python}")
print(f"Chemistry:  {chem}")
print(f"English:  {eng}")
print(f"Physics:  {phy}")
print(f"Percentage: {percentage}%")
print(f"CGPA:{cgpa}")
print(f"Grade: {grade}")
