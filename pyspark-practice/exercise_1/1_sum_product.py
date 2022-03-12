# There are two numbers given below.
# Print the sum of these numbers if their product is greater than 100.
# Otherwise, print their product.
#
# a = 15
# b = 12
#
# Expected Output:
# 27

a = 15
b = 12

product = a * b

if product > 100:
    sum = a + b
    print(sum)
else:
    print(product)
