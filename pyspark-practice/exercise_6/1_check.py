# Question 1:
# Write a Python function to check whether the number given below is present in between 5 to 10 (both included) or not.
# num = 7
# Expected Output:
# 7 is present between 5-10.


num = 7

if 10 >= num >= 5:
    print('{} is present between 5-10.'.format(num))
else:
    print('{} is not present between 5-10.'.format(num))
