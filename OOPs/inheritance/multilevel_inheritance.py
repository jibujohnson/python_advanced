class Grandfather:
    def house(self):
        print("Grandfather's house...")
class Father(Grandfather):
    def bike(self):
        print("Father's bike...")
class Son(Father):
    def laptop(self):
        print("Son's laptop...")

obj1=Son()
obj1.laptop()
obj1.bike()
obj1.house()