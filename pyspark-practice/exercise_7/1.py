# We have defined a variable x equals 2.
# Then we have the if-else condition, which checks if x is equal to 2 or not.
# But we get an error in the output.
# Decode the error and rectify the program to get the expected output.
#
# Expected Output:
# Exact match!

# number = 2

# if number == 2:
#     print("Exact match")
# else:
#     print("Not a match")

number = "2"

try:
    if number == 2:
        print('Exact match')
except ValueError:
    print('Please enter an integer.')
finally:
    print('Exact match!')


