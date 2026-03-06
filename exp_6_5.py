'''5. Write a lambda function to find volume of cone. '''
volume_cone=lambda r,h:(1/3)*3.14159*r*r*h
r=float(input("Enter radius:"))
h=float(input("Enter height:"))
print("Volume of cone:",volume_cone(r,h))