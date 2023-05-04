# Update the Student Class to include these attributes - first_name, last_name, age, country
#   Add these methods to the Student class
#  - show_full_name
#  - year_of_birth
#  - show_initial
class Student:
    school = "AkiraChix"
    def __init__(self,first_name,last_name,age,year_of_birth,country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.year_of_birth = year_of_birth
    def show_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def year_of_birth(self):
        current_year = current_year.age.now().year
        return current_year - self.age
    

    def show_initials(self):
        return f"{self.first_name[0]} {self.last_name[0]}"
    

    

    






  
    
    
    
    
    
   

    



