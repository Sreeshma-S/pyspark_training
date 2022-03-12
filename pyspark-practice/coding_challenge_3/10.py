# We have a list given below, which contains several numbers.
# I want to slice this list based on its indexes, into 3 equal sub-lists.
# num_list = [31, 24, 2, 16, 19, 45, 75, 63, 79]
# Expected Output:
# Sub-List 1 [31, 24, 2]
# Sub-List 2 [16, 19, 45]
# Sub-List 3 [75, 63, 79]

num_list = [31, 24, 2, 16, 19, 45, 75, 63, 79]

sub_list_1 = num_list[:3]
print("sub_list_1", sub_list_1)

sub_list_2 = num_list[3:6]
print("sub_list_2", sub_list_2)

sub_list_3 = num_list[6:9]
print("sub_list_3", sub_list_3)