# Print all the numbers between 1 and 100 (both being included) that are multiples of 3 and 5 both.
# Expected Output:
# Multiples of 3 and 5: [15, 30, 45, 60, 75, 90]

nums = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        nums.append(i)

print("Multiples of 3 and 5:", nums)