# 2. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    num1=int(input("Enter 1st no.:"))
    num2=int(input("Enter 2nd no.:"))
    print(num1/num2)
except ZeroDivisionError:
    print("You cannot divide a number by zero.")