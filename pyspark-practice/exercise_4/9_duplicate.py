# Remove all the duplicate items from the tuple given below.
#
# myTuple = ('Red', 'Blue', 'Green', 'Red', 'Orange', 'Green')
#
# Expected Output:
# {'Blue', 'Green', 'Orange', 'Red'}

myTuple = ('Red', 'Blue', 'Green', 'Red', 'Orange', 'Green')
print(set(myTuple))