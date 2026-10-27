class Shape:
    def draw(self):
        print("Drawing a shape...")
class Circle(Shape):
    def draw(self):
        print("Drawing a circle...")

obj1=Shape()        #Parent class object
obj1.draw()

obj2=Circle()       #Child class object
obj2.draw()