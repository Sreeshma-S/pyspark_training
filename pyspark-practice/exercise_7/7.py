# Write a function to reverse a string if it's length is an even number. ' \
# 'I think of the TypeError exception if a numeric value is passed inside the function call. ' \
# But there might be other exceptions too that can occur while executing the program.
# So, wrap the function around a try-except block and handle the TypeError exception with the message 'Check the string.'
# For all other exceptions, print the message 'Something went wrong.'
# Input String = 'Python'
# Expected Output:¶
# nohtyP


def reverse_string(txt):
    try:
        print(txt[::-1])
    except TypeError:
        print("Check the string")
    except:
        print("Something went wrong")


txt_input = "Python"
# txt_input = 12232332

reverse_string(txt_input)
