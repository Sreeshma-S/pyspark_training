# We have a function given below that adds elements of two lists.
# However, I can think of two exceptions that can occur in this program.
# The index entered by the user during the function call may be out of bound.
# The list entered by the user can consist of int objects, str objects, or even a combination of both.
# And what if we try to add an int object and an str object?
# Re-write this program to handle the two exceptions mentioned above.
#
# Expected Output:
# Invalid index, try again

list_1 = [10, 20, 30]
list_2 = [15, 10, 5, 'descending']

def add(index_1, index_2):
    try:
        sum = list_1[index_1] + list_2[index_2]
        print(sum)
    except IndexError:
        print("Error : Invalid index, try again")
    except TypeError:
        print("Error : Unsupported data type")

add(2, 3)