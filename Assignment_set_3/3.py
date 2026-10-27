# 3. Write a Python program that prompts the user to input an integer and raises a ValueError exception
# if the input is not a valid integer.

try:
    num=int(input("Enter a number:"))
    print("You entered:",num)
except ValueError:
    print("Your value is not an integer. Please enter a valid integer value.")