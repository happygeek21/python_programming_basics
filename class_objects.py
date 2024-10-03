
class Cars:  # Class Declaration

    def __init__(self,name,brand,model,encap): # Constructor, __init__ is a function which is called by default. shown for ref.
        
        self.brand=brand  #variable brand reffering to the constructor (self).
        self.model=model
        self.encap=encap
        self.name=name
        
    def welcome(self): ## This is a method.
        print("Welcome Back!!" ,self.brand)

    def get_ncap(self):

        return self.encap    
    @staticmethod       #@staticmethod is a decorator which is used when we do not need to use any objects/attributes, here we use this method in class level.
    def hello():        
        
        print("Hello")

    def hello_world(self):  #an example of

        print("Hello World",self.name)



car1 = Cars("Karan","VW","Virtus","5Str") # First Object.

print( car1.brand ,car1.model) #printing the data

car2 = Cars("Kabir","Mahindra","ScorpioN","5Str") # Second Object.

print(car2.brand, car2.model) 


car1.welcome()

print(car1.get_ncap())

car1.hello()

car1.hello_world()