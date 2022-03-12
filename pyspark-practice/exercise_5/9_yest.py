# Write a Python program to print yesterdays' date.
# Expected Output:
# Yesterday : 2020-10-16

from datetime import date, timedelta
print(date.today() + timedelta(days=-1))
