''' 
1.Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by               
taking inputs from the user and display details of all students. '''
class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print("Name:",self.name)
        print("SAP ID:",self.sap_id)
        print("Physics:",self.phy)
        print("Chemistry:",self.chem)
        print("Maths:",self.maths)
        print("Total:",self.phy+self.chem+self.maths)
        print("------------------------")

students=[]

for i in range(3):
    print("Enter details of student",i+1)

    name=input("Enter name:")
    sap_id=int(input("Enter SAP ID:"))
    phy=float(input("Enter Physics marks:"))
    chem=float(input("Enter Chemistry marks:"))
    maths=float(input("Enter Maths marks:"))

    s=Student(name,sap_id,phy,chem,maths)
    students.append(s)

    print()

print("\n--- Student Details ---\n")

for s in students:
    s.display()