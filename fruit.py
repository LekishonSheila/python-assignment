class Fruit:
    is_fruit = True
    
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste
    
    def describe(self):
        print(f"This {self.color} {self.name} tastes {self.taste}.")
    
    def eat(self):
        print(f"You ate the {self.name}.")
    
    def rot(self):
        print(f"The {self.name} has started  rotting.")


