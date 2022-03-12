# Here we have a list of 3 letters.
# I want you to concatenate this list with another list of numbers whose range varies from 1 to 3 (3 is included).
# letters_list = ['H', 'R', 'S']
# Expected Output:
# ['H1', 'R1', 'S1', 'H2', 'R2', 'S2', 'H3', 'R3', 'S3']


letters_list = ['H', 'R', 'S']
numbers_list = [1, 2, 3]

alphanumeric_list = []
for i in letters_list:
    for j in numbers_list:
        alphanumeric_list.append(str(i)+str(j))

print(alphanumeric_list)