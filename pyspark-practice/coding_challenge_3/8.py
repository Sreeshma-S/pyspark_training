# Write a program to print all the numbers between 100 to 300 (both included) such that each digit of the given number is an even number.
# Expected Output:
# 200, 202, 204, 206, 208, 220, 222, 224, 226, 228, 240, 242, 244, 246, 248, 260, 262, 264, 266, 268, 280, 282, 284, 286, 288

for i in range(100, 301):
    first_digit = int(str(i)[0])
    sec_digit = int(str(i)[1])
    third_digit = int(str(i)[2])
    if first_digit % 2 == 0 and sec_digit % 2 == 0 and third_digit % 2 == 0:
        print(i)
