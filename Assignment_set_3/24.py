# 24. Calculate number of days between two given dates.

from datetime import datetime
date1=input("Enter first date(DD-MM-YYYY):")
date2=input("Enter second date(DD-MM-YYYY):")
date1=datetime.strptime(date1,"%d-%m-%Y")
date2=datetime.strptime(date2,"%d-%m-%Y")
difference=date2-date1
print("Number of days:",abs(difference.days))