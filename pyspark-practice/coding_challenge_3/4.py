# Write a Python program to print the dates of yesterday, today, and tomorrow.
# Expected Output:
# Yesterday : 2020-10-12
# Today : 2020-10-13
# Tomorrow : 2020-10-14

from datetime import date, timedelta

given_date = date.today()

print("Yesterday : ", given_date + timedelta(days=-1))
print("Today : ", given_date)
print("Tomorrow : ", given_date + timedelta(days=1))

