# You have two dictionaries, with each of them containing several letters associated with certain values.
# num_1 = {'a' : 5, 's' : 7, 'x' : 11, 'm' : 12, 'o' : 8}
# num_2 = {'r' : 12, 'x' : 9, 'n' : 8, 'm' : 12, 'q' : 10}
# I want you to perform the below-mentioned operations on these dictionaries:
# 1. Print out the letters which are common to both these dictionaries.
# 2. Print out the (key, value) pair, which is common to both these dictionaries.
# 3. Print out all the letters which have occurred only once in these dictionaries.
# 4. Print out the letters in num_1 that are not present in num_2.
# 5. Print out a new dictionary num_3, which contains unique letters of num_1 from the previous output with their
#    associated values.
# Expected Output:
# 1. {'x', 'm'}
# 2. {('m', 12)}
# 3. {'o', 'a', 'n', 'q', 'r', 's'}
# 4. {'o', 'a', 's'}
# 5. {'o': 8, 'a': 5, 's': 7}

num_1 = {'a' : 5, 's' : 7, 'x' : 11, 'm' : 12, 'o' : 8}
num_2 = {'r' : 12, 'x' : 9, 'n' : 8, 'm' : 12, 'q' : 10}

set_1 = set(num_1)
set_2 = set(num_2)

common = []
for i in set_1.intersection(set_2):
    common.append(i)
print("1. ", set(common))

num_tuple = ()
for key1, value1 in num_1.items():
    for key2, value2 in num_2.items():
        if key1 == key2 and value1 == value2:
            num_tuple = (key1 , value1)
            print("2. ", num_tuple)

set_key_1 = set(num_1)
set_key_2 = set(num_2)

print("3. ", set(set(set_key_1).symmetric_difference(set(set_key_2))))

print("4. ", set(set(set_key_1).difference(set(set_key_2))))

print("5. ", set(num_1.items()) - set(num_2.items()))