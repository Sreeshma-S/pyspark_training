# Print today's date in the format given below.
# Day_name Day_number Month_name Year
# Expected Output:
# Today's date is: Tuesday 13 October 2020


from datetime import datetime

given_date = datetime.now()

print("Today's data is: {} {} {} {}".format(given_date.strftime('%A'), given_date.day, given_date.strftime("%B"), given_date.year))

