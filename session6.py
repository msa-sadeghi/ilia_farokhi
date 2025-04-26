class Vehicle:
    def __init__(self, name, model, year, color):
        self.name = name
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f"name={self.name}, model={self.model}, year={self.year}, color={self.color}"
    def move(self):
        print(f"{self.name} is moving")
    def stop(self):
        print(f"{self.name} has stopped")

class Car(Vehicle):
    def __init__(self, name, model, year, color, doors=4):
        super().__init__(name, model, year, color)
        self.doors = doors

    def something(self):
        print(f"{self.name} is doing something")

class Truck(Vehicle):
    def __init__(self, name, model, year, color, capacity):

        super().__init__(name, model, year, color)
        self.capacity = capacity
    def load(self, weight):
        if weight <= self.capacity:
            print(f"{self.name} is loading {weight} kg")
        else:
            print(f"{self.name} cannot load {weight} kg, exceeds capacity of {self.capacity} kg")

class Bus(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass


car1 = Car("Toyota", "Corolla", 2020, "Red")
car1.move() 