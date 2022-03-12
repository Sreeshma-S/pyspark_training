# Print the number and the cube of that number in a dictionary from 0 to 5.
# Expected Output:
# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

cubes = []
num = [0, 1, 2, 3, 4, 5]
for i in range(0,6):
    cubes.append(i**3)

print(dict(zip(num, cubes)))
