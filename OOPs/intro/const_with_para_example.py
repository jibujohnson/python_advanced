class Employee:
    def __init__(self,id,name,place,company,salary,designation):
        self.employee_id=id
        self.employee_name=name
        self.employee_company=company
        self.employee_place=place
        self.employee_designation=designation
        self.employee_salary=salary
    def display_employee_details(self):
        print("__Employee Details__")
        print("ID:",self.employee_id)
        print("Name:",self.employee_name)
        print("Place:",self.employee_place)
        print("Company:",self.employee_company)
        print("Salary:",self.employee_salary)
        print("Designation:",self.employee_designation)

obj1=Employee(101,"Ashwin","Koonamavu","InfoPark",5000,"Staff")
obj1.display_employee_details()
obj2=Employee(102,"Aljin","Thrissur","InfoPark",10000,"Staff")
obj2.display_employee_details()
obj3=Employee(103,"Gautham","Thrissur","InfoPark",15000,"Staff")
obj3.display_employee_details()