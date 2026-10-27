# 10) Write a Python function to multiply all the numbers in a list.

def multiply_list(numbers):
    result=1
    for i in numbers:
        result=result*i
    return result

n=int(input("Enter the number of elements:"))
numbers=[]
for i in range(n):
    numbers.append(int(input("Enter number:")))
result=multiply_list(numbers)
print("Product:",result)