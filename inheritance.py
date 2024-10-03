class Car():  # This is the parent class.

    @staticmethod
    def car_start():
        print("Car Started...")  # Static method to start the car.

    @staticmethod
    def car_stop():
        print("Car Stopped...")  # Static method to stop the car.

class Brand(Car):  # Brand class inherits from Car.

    def __init__(self, name):
        self.name = name  # Initialize the name attribute.
        self.car_start()  # Call the static method to indicate the car has started.

class Model(Brand):  # Model class inherits from Brand, demonstrating multilevel inheritance.

    def __init__(self, name, model):
        super().__init__(name)  # Call the constructor of the Brand class to initialize name.
        self.model = model  # Initialize the model attribute.

class MakeYear(Model):  # MakeYear class inherits from Model.

    def __init__(self, name, model, year):
        super().__init__(name, model)  # Call the constructor of the Model class to initialize name and model.
        self.year = year  # Initialize the year attribute.

# Creating an instance of MakeYear with specified parameters.
car1 = MakeYear("Maruti", "Swift", "2005")

# Print the attributes of the car1 object.
print(car1.name)   # Outputs: Maruti
print(car1.model)  # Outputs: Swift
print(car1.year)   # Outputs: 2005
