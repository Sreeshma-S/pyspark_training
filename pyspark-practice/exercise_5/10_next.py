# Write a Python program to print the next 5 days from the date given below.
# given_date = datetime(2020, 10, 17)
# Expected Output:
# 2020-10-18 00:00:00
# 2020-10-19 00:00:00
# 2020-10-20 00:00:00
# 2020-10-21 00:00:00
# 2020-10-22 00:00:00

from datetime import datetime, timedelta

given_date = datetime(2020, 10, 17)

print(given_date + timedelta(days=1))
print(given_date + timedelta(days=2))
print(given_date + timedelta(days=3))
print(given_date + timedelta(days=4))
print(given_date + timedelta(days=5))