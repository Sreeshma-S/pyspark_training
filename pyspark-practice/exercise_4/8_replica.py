# We have a dictionary given below.
# Copy this dictionary into another dictionary 'replica,' and change the value of the key 103 to 'Sally' in the replica dictionary only. Finally, print both the dictionaries.
# student_details = {101:'Judy', 102:'Victor', 103:'Sam'}
# Expected Output:
# {101: 'Judy', 102: 'Victor', 103: 'Sam'}
# {101: 'Judy', 102: 'Victor', 103: 'Sally'}


student_details = {101:'Judy', 102:'Victor', 103:'Sam'}

student_details_copy = student_details.copy()


student_details_copy[103] = "Sally"

print(student_details)
print(student_details_copy)

