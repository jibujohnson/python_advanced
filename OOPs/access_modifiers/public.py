class Company:
    def __init__(self):
        self.company_name="Luminar Technolab"       #Public variable
    def display_company_info(self):                 #Public member function
        print("Company Name:",self.company_name)    #Accessing inside the class

class Employee(Company):
    def display_employee_info(self):
        print("Company name:",self.company_name)    #Accessing in the child class

object1=Company()                   #Parent class object
object1.display_company_info()

object2=Employee()                  #Child class object
object2.display_employee_info()

print(object1.company_name)         #Accessing outside the class
