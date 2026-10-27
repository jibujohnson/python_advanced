class Student:
    def __init__(self,name,age,course,mark):
        self.name=name
        self.age=age
        self.course=course
        self.mark=mark
    def display(self):
        print("STUDENT DETAILS")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Course:",self.course)
        print("Mark:",self.mark)

student=Student("Jibu",20,"BCA",54)
student.display()
student1=Student("Jithu",26,"+2",80)
student1.display()