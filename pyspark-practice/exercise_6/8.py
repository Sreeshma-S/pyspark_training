# Write a Python program to add the three lists given below using Python map and Lambda function.
# list_1 = [1, 5, 8]
# list_2 = [3, 2, 5]
# list_3 = [2, 3, 6]
# Expected Output:
# Resultant List: [6, 10, 19]

list_1 = [1, 5, 8]
list_2 = [3, 2, 5]
list_3 = [2, 3, 6]

output_list = []
for i in range(0, len(list_1)):
    x = lambda list1, list2, list3: list_1[i] + list_2[i] + list_3[i]
    output_list.append(x(list_1, list_2, list_3))

print(output_list)

