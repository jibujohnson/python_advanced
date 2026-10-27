# 15. Write a Python program to print the next 5 days starting today.

from datetime import date,timedelta
today=date.today()
for i in range(5):
    next_day=today+timedelta(days=i)
    print(next_day)