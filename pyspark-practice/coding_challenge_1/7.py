# We have a list of lists that contains several numbers.
# I want you to print the list whose sum of elements is the highest and also the lowest.
# num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]
# Expected Output:
# The list with the maximum sum of elements: [19, 13, 7]
# The list with the minimum sum of elements: [2, 8, 11]

num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]

dict = {}
for i in num_list:
    dict[sum(i)] = i
print("The list with the maximum sum of elements: ", dict[max(dict)])
print("The list with the minimum sum of elements: ", dict[min(dict)])
