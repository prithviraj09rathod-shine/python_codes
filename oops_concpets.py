#class, object, Inheritance, polymorphism
#from pyexpat import model
class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")

class motorcycle(vehicle):
    def move(self):
        print("Ride!")

#ex: of multiple inheritance
class truck(vehicle):
    pass

class bus(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.level = "8 wheeler"

'''polymorphism example when different classes have same method name move()
and executed particular move() based on, which object is calling it'''
class car:
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model  
    def move(self):
        print("Move!")

class Boat:
    def __init__(self, brand, model) :
        self.brand = brand
        self.model = model  
    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model  
    def move(self):
        print("Fly!")

#inherited class object creation
moto1 = motorcycle("Harley-Davidson", "Street 750") #Create a
truck1 = truck("Ford", "F-150")   #Create a Truck object
bus1 = bus("Volvo", "7700")        #Create a Bus object

car1 = car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object   
plane1 = Plane("Boeing", "747")     #Create a Plane object
for x in (car1, boat1, plane1):
    x.move()

'''Inheritance example-deriving/inheriting properties from a parent class.
Here Vehicle --> is the parent class and 
Car, Boat, Plane --> are the child classes'''