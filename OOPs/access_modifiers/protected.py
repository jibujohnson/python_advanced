class Student:
    def __init__(self):
        self._marks=92                      #Protected variable
    def display(self):
        print("Marks:",self._marks)         #Accessing in the same class

class Myclass(Student):
    def student_data(self):
        print("___STUDENT DETAILS___")
        print("Total marks:",self._marks)   #Accessing in the child class

obj=Myclass()
obj.display()
obj.student_data()

print(obj._marks)                           #Accessing is possible outside the class