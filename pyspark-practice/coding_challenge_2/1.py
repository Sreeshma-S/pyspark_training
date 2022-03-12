# We have two lists of numbers given below.
# I want you to create a third list by picking an odd-indexed element from the first list and even-indexed elements from the second list.
# list_1 = [5, 10, 15, 20, 25, 30, 35]
# list_2 = [7, 14, 21, 28, 35, 42, 49]
# Expected Output:
# [10, 20, 30, 7, 21, 35, 49]

list_1 = [5, 10, 15, 20, 25, 30, 35]
list_2 = [7, 14, 21, 28, 35, 42, 49]

new_list_1 = list_1[1::2]
new_list_2 = list_2[0::2]
print(new_list_1 + new_list_2)
