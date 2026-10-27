class College:
    def __init__(self):
        self.college_name=""
        self.location=""
        self.contact_number=""
    def college_data(self):
        self.college_name=input("Enter College name:")
        self.location=input("Enter Location:")
        self.contact_number=input("Enter contact number:")
    def college_info(self):
        print("__College Details__")
        print("College name:",self.college_name)
        print("Location:",self.location)
        print("Contact_number:",self.contact_number)

class Department(College):
    def __init__(self):
        self.dept_id=""
        self.dept_name=""
        self.HOD=""
    def department_data(self):
        self.dept_id=int(input("Enter Department ID:"))
        self.dept_name=input("Enter Department name:")
        self.HOD=input("Enter HOD name:")
    def department_info(self):
        print("__Department Details__")
        print("Department ID:",self.dept_id)
        print("Department name:",self.dept_name)
        print("Department HOD:",self.HOD)

class Student(Department):
    def __init__(self):
        self.stud_id=""
        self.name=""
        self.course=""
        self.place=""
        self.mobile=""
    def student_data(self):
        self.stud_id=int(input("Enter Student ID:"))
        self.name=input("Enter Student name:")
        self.course=input("Enter the Course:")
        self.place=input("Enter the place:")
        self.mobile=input("Enter mobile number:")
    def student_info(self):
        print("__Student Details__")
        print("Student ID:",self.stud_id)
        print("Student name:",self.name)
        print("Course:",self.course)
        print("Place:",self.place)
        print("Mobile.no:",self.mobile)

obj=Student()
obj.college_data()
obj.department_data()
obj.student_data()

obj.college_info()
obj.department_info()
obj.student_info()