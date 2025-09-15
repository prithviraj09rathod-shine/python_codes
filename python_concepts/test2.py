#OOPs concepts implementation in Python
class Car:
    def __init__(self, make, model, year):
        self.make = make    
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()    
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.") 
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles  
        if miles < 0:
            print("You can't increment the odometer with negative miles!") 

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75  
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100
            print("Battery upgraded to 100 kWh.")
        else:
            print("Battery is already at maximum capacity.")

# Example usage: Inheritance(helfful for achieveing reusabality) and method overriding
class GasolineCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.fuel_tank_size = 15  
    
    def describe_fuel_tank(self):
        print(f"This car has a {self.fuel_tank_size}-gallon fuel tank.")
    
    def get_fuel_range(self):
        range = self.fuel_tank_size * 25  
        print(f"This car can go about {range} miles on a full tank.")  

                                                                                          

my_tesla = ElectricCar('tesla', 'model s', 2020)
print(my_tesla.get_descriptive_name())  
my_tesla.describe_battery()
my_tesla.get_range()        
my_tesla.upgrade_battery()
my_tesla.get_range()    
my_tesla.update_odometer(15000)
my_tesla.read_odometer()    
my_tesla.increment_odometer(500)

