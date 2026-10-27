# 7. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

obj=Calculator()
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Addition:",obj.add(num1,num2))
print("Subtraction:",obj.subtract(num1,num2))
print("Multiplication:",obj.multiply(num1,num2))
print("Division:",obj.divide(num1,num2))