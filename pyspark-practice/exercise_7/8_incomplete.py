# Write a function to extract the first ten letters of a string passed as an argument.
# But if the string is less than ten characters long, raise a ValueError and handle it using the message 'Oops! Too short string.'
# Expected Output:
# Oops! Too short string.


def extract_string(txt):
    # if len(txt) > 9:
        try:
            print(txt[0:10:1])
        except ValueError:
            print("Oops! Too short string.")

txt_input = "Python Basics"
# txt_input = "Python"

extract_string(txt_input)
