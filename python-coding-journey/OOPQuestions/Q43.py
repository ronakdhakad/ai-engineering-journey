# 43. Demonstrate Inheritance
# Animal
# Dog
# Cat

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
a=Animal()
a.sound()
d.sound()   # inherited from Animal
d.bark()

c.sound()   # inherited from Animal
c.meow()
