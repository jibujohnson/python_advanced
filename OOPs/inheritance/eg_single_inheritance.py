class Company:
    def __init__(self):
        self.company_name=""
        self.company_location=""
    def company_data(self):
        self.company_name=input("Enter Company name:")
        self.company_location=input("Enter Company location:")
    def company_info(self):
        print("__Company Details__")
        print("Company name:",self.company_name)
        print("Company location:",self.company_location)

class Employee(Company):
    def __init__(self):
        self.name=""
        self.email=""
        self.designation=""
        self.place=""
    def employee_data(self):
        self.name=input("Enter Employee name:")
        self.email=input("Enter Employee email:")
        self.designation=input("Enter Employee designation:")
        self.place=input("Enter Employee place:")
    def employee_info(self):
        print("__Employee Details__")
        print("Employee name:",self.name)
        print("Employee email:",self.email)
        print("Employee designation:",self.designation)
        print("Employee place:",self.place)

obj1=Employee()
obj1.employee_data()
obj1.company_data()
obj1.employee_info()
obj1.company_info()