# We have two lists given below.
# I want you to print the first list in the original order and the second list in reverse order simultaneously.
# list_1 = [12, 25, 31, 20, 18]
# list_2 = [11, 9, 43, 22, 55]
# Expected Output:
# 12 55
# 25 22
# 31 43
# 20 9
# 18 11


list_1 = [12, 25, 31, 20, 18]
list_2 = [11, 9, 43, 22, 55]

list_2.sort(reverse=True)

for i in zip(list_1, list_2):
    print(i)