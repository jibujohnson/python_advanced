# 5. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math
class Circle:
    def __init__(self):
        self.radius=0
    def area(self):
        return math.pi*self.radius*self.radius
    def perimeter(self):
        return 2*math.pi*self.radius

obj=Circle()
obj.radius=float(input("Enter the radius:"))
print("Area:",obj.area())
print("Perimeter:",obj.perimeter())