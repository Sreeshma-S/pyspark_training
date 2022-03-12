# Write a program to process the results of the user.
# The program should consist of a user-defined exception class 'InvalidNumError' to raise an error
# if the marks entered by the user is less than 0 or greater than 100.
# Otherwise, print the message 'Results processing.'
# Expected Output:
# Results processing.
# Error! Try again.

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidNumError(Error):
    print("Error! Try again.")
    pass


mark = 10

try:
    if 100 >= mark >0:
        print("Results processing")
    else:
        raise InvalidNumError
except InvalidNumError:
    print("Error! Try again.")

