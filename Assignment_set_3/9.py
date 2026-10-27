# 9) Write a Python function to sum all the numbers in a list.

def sum_list(numbers):
    total=0
    for i in numbers:
        total=total+i
    return total

n=int(input("Enter the number of elements:"))
numbers=[]
for i in range(n):
    numbers.append(int(input("Enter number:")))
result=sum_list(numbers)
print("Sum:",result)
