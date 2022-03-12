# We have a set that contains roll numbers of candidates who have applied for an event.
# Out of the applied candidates, few have submitted their application forms, and we have registered their details in a dictionary given below.
# Print the roll numbers of the candidates who have submitted their application forms and also the ones who are yet to submit it.
# roll_numbers = {12, 7, 15, 23, 32, 30}
# student_details = {12:'Judy', 30:'Shane', 23:'Aaron'}
# Expected Output:
# Completed Applications: {12, 30, 23}
# Pending Applications: {32, 15, 7}

roll_numbers = {12, 7, 15, 23, 32, 30}
student_details = {12:'Judy', 30:'Shane', 23:'Aaron'}

completed_list = []
for key in student_details:
    completed_list.append(key)
    pending = set(roll_numbers) - set(completed_list)


print("Completed Applications: ", completed_list)
print("Pending Applications: ", pending)
