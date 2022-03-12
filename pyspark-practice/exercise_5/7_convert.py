# Write a Python program to convert a string to datetime.
# myString = Oct 12 2002 12:45 PM
# Expected Output:
# 2002-10-12 12:45:00

from datetime import datetime

myString = 'Oct 12 2002 12:45 PM'

result = datetime.strptime(myString, '%b %d %Y %I:%M %p')

print(result)