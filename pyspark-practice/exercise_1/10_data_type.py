# I have an examination form that requires the following information.
# Name, Age, Roll Number, and Subjects.
# Declare the parameters mentioned above with a suitable data type, and then assign some values to it, and finally print the result.
# Expected Output:
# Name: Sachin
# Age: 17
# Roll Number: 528841
# Subjects: ['Maths', 'Physics', 'Chemistry', 'Computer Science', 'English']

def exam_form(name, age, roll, sub):
    name = str(name)
    age = int(age)
    roll_number = int(roll)
    subject = list(sub)

    print('Name: {}'.format(name))
    print('Age: {}'.format(age))
    print('Roll Number: {}'.format(roll_number))
    print('Subjects: {}'.format(subject))

exam_form("Sachin", 17, 528841,  ['Maths', 'Physics', 'Chemistry', 'Computer Science', 'English'])