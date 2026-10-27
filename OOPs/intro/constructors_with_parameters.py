class Student:                                          #Class
    def __init__(self,name,course):                     #Constructor method
        self.student_name=name                          #Attribute1
        self.student_course=course                      #Attribute2
    def display(self):                                  #Method
        print("__Student Details__")
        print("Name:",self.student_name)
        print("Course:",self.student_course)

obj1=Student("Jibu","Python")
obj1.display()
obj2=Student("Aljin","MEARN")
obj2.display()