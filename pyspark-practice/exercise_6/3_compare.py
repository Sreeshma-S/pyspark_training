# Create a function in Python that displays the name and results of a candidate.
# The function should accept the candidate's name and his/her results as "Pass/Fail." ' \
# If the result is missing in the function call, show it as "Pass."
# Expected Output:
# Sam is Pass.
# Judy is Fail

def calculate(name, status):
    if status == '':
        status = 'Pass'
    else:
        status = status
        name = name

    print("{} is {}".format(name, status))


calculate('Sam', '')
calculate('Judy', 'Fail')