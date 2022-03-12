# We have a number given below. Write a program to check for the divisibility of this number by 3 and 5, and print the result obtained.
# a = 12
# Expected Output:
# a is divisible by either 3 or 5, but not both


a = 12

if a % 3 == 0 and a % 5 == 0:
    print("a is divisible by both 3 and 5")
elif a % 3 == 0:
    print("a is divisible by 3")
elif a % 5 == 0:
    print("a is divisible by 5")
else:
    print("a is divisible by neither 3 nor 5")


