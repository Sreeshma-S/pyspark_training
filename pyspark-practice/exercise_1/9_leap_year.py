# Write a Python program to check if the given year is a leap year.
# year = 1996
# Expected Output:
# Leap Year

year = 1996

if (int(year) % 100 == 0):
    if (int(year) % 400 == 0):
        print("Leap year")
    else:
        print("Given year is not a leap year")
elif (int(year) % 4 == 0):
    print("Leap year")
else:
    print("Given year is not a leap year")

