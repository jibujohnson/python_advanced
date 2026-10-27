# MULTILEVEL INHERITANCE
#
# class Hospital:
#     hospital name,location,contact
# class Department(Hospital):
#     id,dept_name,hod name
# class Patient(Department):
#     p_id,name,age,place,illness,contact

class Hospital:
    def __init__(self):
        self.hospital_name=""
        self.location=""
        self.contact=""
    def hospital_data(self):
        self.hospital_name=input("Enter Hospital name:")
        self.hospital_location=input("Enter Hospital location:")
        self.hospital_contact=int(input("Enter Hospital contact number:"))
    def hospital_info(self):
        print("\n-----HOSPITAL DETAILS-----")
        print("Hospital Name:",self.hospital_name)
        print("Hospital Location:",self.hospital_location)
        print("Contact.no:",self.hospital_contact)

class Department(Hospital):
    def __init__(self):
        self.dept_id=""
        self.dept_name=""
        self.hod_name=""
    def department_data(self):
        obj.hospital_data()
        self.dept_id=int(input("Enter Department ID:"))
        self.dept_name=input("Enter Department name:")
        self.hod_name=input("Enter HOD name:")
    def department_info(self):
        obj.hospital_info()
        print("\n-----DEPARTMENT DETAILS-----")
        print("Department_ID:",self.dept_id)
        print("Department name:",self.dept_name)
        print("HOD name:",self.hod_name)

class Patient(Department):
    def __init__(self):
        self.patient_id=""
        self.patient_name=""
        self.patient_age=""
        self.patient_place=""
        self.patient_illness=""
        self.patient_contact=""
    def patient_data(self):
        obj.department_data()
        self.patient_id=int(input("Enter patient ID:"))
        self.patient_name=input("Enter patient name:")
        self.patient_age=int(input("Enter patient age:"))
        self.patient_place=input("Enter patient place:")
        self.patient_illness=input("Enter patient illness:")
        self.patient_contact=int(input("Enter patient contact:"))
    def patient_info(self):
        obj.department_info()
        print("\n-----PATIENT DETAILS-----")
        print("Patient ID:",self.patient_id)
        print("Patient name:",self.patient_name)
        print("Patient age:",self.patient_age)
        print("Patient place:",self.patient_place)
        print("Patient illness:",self.patient_illness)
        print("Patient contact:",self.patient_contact)

obj=Patient()
obj.patient_data()
obj.patient_info()