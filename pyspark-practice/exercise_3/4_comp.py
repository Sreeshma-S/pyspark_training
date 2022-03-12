# We have a list of numbers given below.
# Print the square of these numbers into another list using list comprehension.
# num = [2, 4, 6, 8]
# Expected Output:
# [4, 16, 36, 64]

num = [2, 4, 6, 8]

newlist = [x**2 for x in num]

print(newlist)