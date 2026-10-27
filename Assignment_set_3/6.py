# 6. Write a Python program to create a person class. Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.
from datetime import date,datetime
class Person:
    def __init__(self):
        self.name=""
        self.country=""
        self.date_of_birth=""
    def person_data(self):
        self.name=input("Enter your name:")
        self.country=input("Enter your country:")
        self.date_of_birth=input("Enter your date of birth(DD-MM-YYYY):")
    def calculate_age(self):
        birth_date=datetime.strptime(self.date_of_birth,"%d-%m-%Y").date()
        today=date.today()
        age=today.year-birth_date.year
        if(today.month,today.day)<(birth_date.month,birth_date.day):
            age=age-1
        return age
    def person_info(self):
        print("*****PERSON DETAILS*****")
        print("Name:",self.name)
        print("Country:",self.country)
        print("Date of birth:",self.date_of_birth)
        print("Age:",self.calculate_age())

obj=Person()
obj.person_data()
obj.person_info()