# We have the marks of a student in each subject given below.
# Write a Python function that takes two parameters 'name' and 'subjects_marks.'
# Finally, print the student's name and all the subjects in which his/her marks are above 60. ' \
# 'If the 'name' is not provided, print 'None.'
#
# Mathematics = 80, Physics = 58, Chemistry = 62, English = 72, Biology = 50
# Expected Output:
# Name: Brandon - Subjects: {'Chemistry', 'English', 'Mathematics'}


# rewriting equation to dictionary

mark_dict = {'Mathematics':80, 'Physics':58, 'Chemistry':62, 'English':72, 'Biology':50}

def show_marks(name, mark):

    if len(name) > 0:
        name = name
    else:
        name = 'None'

    final_subject_arr = []
    for key, value in mark.items():
        if value > 60:
            final_subject_arr.append(key)

    print("Name : {} - Subjects : {}".format(name, set(final_subject_arr)))

show_marks('Brandon', mark_dict)