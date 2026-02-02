'''
5. Check whether the quadratic equation has real roots or imaginary roots. Display the 
roots.
'''
a=int(input("Enter coefficient a: "))
b=int(input("Enter coefficient b: "))
c=int(input("Enter coefficient c: "))
if a==0:
    print("Not a quadratic equation.")
else:
    d=b**2 - 4*a*c
    if d > 0:
        root1 = (-b + d**0.5) / (2*a)
        root2 = (-b - d**0.5) / (2*a)
        print(f"The equation has real and distinct roots: {root1} and {root2}")
    elif d == 0:
        root = -b / (2*a)
        print(f"The equation has real and equal roots: {root}")
    else:
        real_part = -b / (2*a)
        imag_part = (-d**0.5) / (2*a)
        print(f"Imaginary roots: {real_part} + {imag_part}i and {real_part} - {imag_part}i")