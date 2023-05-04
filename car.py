class Car:
    wheels = 4
    
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def start_engine(self):
        print(f"The {self.color} {self.make} {self.model} has started moving.")
    
    def drive(self):
        print(f"The {self.color} {self.make} {self.model} is driving.")
    
    def stop(self):
        print(f"The {self.color} {self.make} {self.model} has brake down.")
