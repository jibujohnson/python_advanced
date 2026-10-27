class Employee:
    def __init__(self):
        self.name="Niketh"
        self.__salary=20000
    def display(self):
        print("NAME:",self.name)
        print("SALARY:",self.__salary)

obj=Employee()
obj.display()

print("Outside the class____")
print(obj.name)
print(obj.__salary)