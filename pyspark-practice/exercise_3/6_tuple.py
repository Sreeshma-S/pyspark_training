# We have a tuple of numbers given below.
# Remove the largest number from the tuple and print it in sorted order.
# num_tuple = (5, 8, 13, 2, 17, 1)


num_tuple = (5, 8, 13, 2, 17, 1)
new_tuple = tuple(sorted(num_tuple))
print(new_tuple[:-1])