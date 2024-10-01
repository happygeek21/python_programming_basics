
class Cars:  # Class Declaration

    def __init__(self,brand,model): # Constructor, __init__ is a function which is called by default. shown for ref.
        
        self.brand=brand  #variable brand reffering to the constructor (self).
        self.model=model
        


car1 = Cars("VW","Virtus") # First Object.

print( car1.brand ,car1.model) #printing the data

car2 = Cars("Mahindra","ScorpioN") # Second Object.

print(car2.brand, car2.model)