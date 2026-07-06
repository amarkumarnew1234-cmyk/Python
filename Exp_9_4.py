# 4. Create a class to implement method Overriding. 
class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Execution
obj1 = Dog()
obj2 = Cat()

obj1.sound()
obj2.sound()