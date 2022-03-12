# Print all the multiples of 3 between 5 and 25.
# Expected Output:
# 6
# 9
# 12
# 15
# 18
# 21
# 24

for i in range(5, 25):
    if i % 3 == 0:
        print(i)
