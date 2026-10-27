# 4. Write a Python program that executes division and handles an ArithmeticError exception
# if there is an arithmetic error.

try:
    num1=int(input("Enter 1st number:"))
    num2=int(input("Enter 2nd number:"))
    print(num1/num2)
except ArithmeticError:
    print("Division Completed")