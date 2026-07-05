# 3. Create programs to implement different types of inheritances.
class A:
    def methodA(self):
        print("Method A")

class B(A):
    def methodB(self):
        print("Method B")

class C(A):
    def methodC(self):
        print("Method C")

class D(B, C):
    def methodD(self):
        print("Method D")

obj = D()
obj.methodA()
obj.methodD()