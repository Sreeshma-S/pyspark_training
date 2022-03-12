# We have a program given below that generates an AttributeError exception.
# Make changes in the program to handle this exception and print the message 'An error occured.'
# Expected Output:
# An error occurred.

dict = {}

try:
    dict.append('string')
    print(dict)
except AttributeError:
    print("An error occured")