# Class is a blueprint of an object
# Object is an instance of a class

class Person:
    #properties/attributes/variables/characteristics
    name = "James"
    age = 45
    gender = "Female"

    # Methods/Fuction/Behaviour
    def move(self):
        print("Person is walking")

farmer = Person()
farmer.move()
print(farmer.gender)
