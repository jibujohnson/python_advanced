# MULTIPLE INHERITANCE
#
# Person:
#        name,age,place,mob.no,email_id
# Salary:
#        basic salary,bonus,date of joining
# Employee(Person,Salary):
#        emp_id,designation

class Person:
    def __init__(self):
        self.name=""
        self.age=""
        self.place=""
        self.mobile=""
        self.email=""
    def person_data(self):
        self.name=input("Enter your name:")
        self.age=int(input("Enter your age:"))
        self.place=input("Enter your place:")
        self.mobile=input("Enter your mobile.no:")
        self.email=input("Enter your email:")
    def person_info(self):
        print("*****DETAILS OF A PERSON*****")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Place:",self.place)
        print("Mobile.no:",self.mobile)
        print("Email id:",self.email)

class Salary:
    def __init__(self):
        self.basic_salary=""
        self.bonus=""
        self.date_of_joining=""
    def salary_data(self):
        self.basic_salary=input("Enter your basic salary:")
        self.bonus=input("Enter your bonus:")
        self.date_of_joining=input("Enter your joining date:")
    def salary_info(self):
        print("*****DETAILS OF SALARY*****")
        print("Basic Salary:",self.basic_salary)
        print("Bonus:",self.bonus)
        print("Date of joining:",self.date_of_joining)

class Employee(Person,Salary):
    def __init__(self):
        self.emp_id=""
        self.designation=""
    def employee_data(self):
        self.emp_id=input("Enter Employee ID:")
        self.designation=input("Enter Employee designation:")
    def employee_info(self):
        print("*****DETAILS OF AN EMPLOYEE*****")
        print("Employee ID:",self.emp_id)
        print("Employee designation:",self.designation)

obj=Employee()
obj.person_data()
obj.salary_data()
obj.employee_data()

obj.person_info()
obj.salary_info()
obj.employee_info()