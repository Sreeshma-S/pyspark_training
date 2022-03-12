# Write a Python program to print the first and the last second of the day.
# Expected Output:
# First Second: 00:00:00
# Last Second: 23:59:59.999999


import datetime
print("First Second: ", datetime.time.min)
print("Last Second: ", datetime.time.max)