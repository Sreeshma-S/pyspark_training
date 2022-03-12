# We have a list of numbers given below.
# Print the number, square of the number, and the cube of the number, all in a single list.
# num = [2, 4, 6, 8]
# Expected Output:
# [(2, 4, 8), (4, 16, 64), (6, 36, 216), (8, 64, 512)]

num = [2, 4, 6, 8]

square = [x**2 for x in num]

cube = [x**3 for x in num]

list = [x for x in zip(num, square, cube)]

print(list)