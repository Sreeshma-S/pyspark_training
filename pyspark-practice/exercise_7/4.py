# We have a function given below which prints an element from the list.
# But what if the user calls an invalid index?
# So, I want you to re-write the following function using the try-except block to handle the IndexError exception.
# Expected Output:
# Invalid index, try again.

fruits = ["apple", "orange", "banana"]
index = 3
try:
    print(fruits[index])
except IndexError:
    print("Invalid index, try again")
