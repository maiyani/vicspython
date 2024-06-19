#parent class/base class/super class

class Animal:
    hasScales = True
    def sound(self):
        print("Animal is speaking")
        #Child class/sub class /Derived classs

class Duck(Animal):
    hasWings = True
    def move(self):
        print("Duck is swimming")

class caterpillar(Duck):
    def move(self):
        print("Caterpilar is slithering")


a = Animal()

d = Duck()
print(d.hasWings)

c = caterpillar()
c.sound()