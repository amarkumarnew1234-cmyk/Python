''' 2. Add constructor in the above class to initialize student details of n students and implement 
following methods: 
a) Display() student details 
b) Find Marks_percentage() of each student 
c)  Display result() [Note: if marks in each subject >40% than Pass else Fail] 
d) Write a Function to find average of the class. '''
class Student:
    def __init__(self,name,sap_id,phy,chem,maths):
        self.name=name
        self.sap_id=sap_id
        self.phy=phy
        self.chem=chem
        self.maths=maths
    def display(self):
        print("Name:",self.name)
        print("SAP ID:",self.sap_id)
        print("Physics:",self.phy)
        print("Chemistry:",self.chem)
        print("Maths:",self.maths)
    def marks_percentage(self):
        return (self.phy+self.chem+self.maths)/3
    def result(self):
        if self.phy>40 and self.chem>40 and self.maths>40:
            return "Pass"
        else:
            return "Fail"
def class_average(students):
    total=0
    for s in students:
        total+=s.marks_percentage()
    return total/len(students)
students=[]
n=int(input("Enter no. of students: "))
for i in range(n):
    print("Enter details of student",i+1)
    name=input("Enter name: ")
    sap_id=int(input("Enter sap id: "))
    phy=float(input("Enter physics marks: "))
    chem=float(input("Enter chemistry marks: "))
    maths=float(input("Enter mathematics marks: "))
    s=Student(name,sap_id,phy,chem,maths)
    students.append(s)
print("\n--- Student Details ---\n")
for s in students:
    s.display()
    print("Percentage:",s.marks_percentage())
    print("Result:",s.result())
    print("------------------------")
avg=class_average(students)
print("\nClass Average Percentage:",avg)