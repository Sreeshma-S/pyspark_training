# Write a Python program to add 2 days and 10 hours to a given date.
# given_date = datetime(2016, 2, 27, 11, 30, 0)
# Expected Output:
# 2016-02-29 21:30:00


from datetime import timedelta, datetime

given_date = datetime(2016, 2, 27, 11, 30, 0)

calculated_date = given_date + timedelta(days=2) + timedelta(hours=10)

print(calculated_date)