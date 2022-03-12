# Write a Python function that accepts two arguments and calculates the addition and subtraction of it.
# Also, print both the arithmetic results in a single return call.
# Expected Output:
# (Addition, Substraction) : (50, 30)


def calculate(input1, input2):
    addition = input1 + input2
    if input1 > input2:
        subtraction = input1 - input2
    else:
        subtraction = input2 - input1

    print("(Addition, Subtraction) : ({}, {})".format(addition, subtraction))

num1 = 10
num2 = 43
calculate(num1, num2)