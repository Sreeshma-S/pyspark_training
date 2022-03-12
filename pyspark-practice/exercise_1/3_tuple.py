# We have the name and seat numbers of a student given below as two tuples.
# With this given data, print the students' names and their assigned seat numbers in a single line using the appropriate data type.
# name = ('Shaun', 'Ron', 'Michael')
# seat_numbers = (101, 102, 103)
# Expected Output:
# {'Shaun': 101, 'Ron': 102, 'Michael': 103}

name = ('Shaun', 'Ron', 'Michael')
seat_numbers = (101, 102, 103)

print(dict(zip(name, seat_numbers)))