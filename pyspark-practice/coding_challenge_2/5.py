# We have two sets given below. Print the first set again after removing the elements common to both of these sets.
# set_1 = {2, 8, 19, 13, 24, 55, 48, 93}
# set_2 = {7, 11, 55, 84, 8, 65, 73, 13}
# Expected Output:
# {2, 48, 19, 24, 93}

set_1 = {2, 8, 19, 13, 24, 55, 48, 93}
set_2 = {7, 11, 55, 84, 8, 65, 73, 13}
print(set_1.difference(set_2))