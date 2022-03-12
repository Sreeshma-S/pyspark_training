# Write a program to square the number entered by the user.
# But what if the user enters a string or an alphanumeric value, or if some other unexpected exceptions occur.
# So, wrap the program inside the try-except block to handle the exceptions, and the program should run until the user enters a numeric value.
# Expected Output:
# Enter a number: aa
# Enter a valid input.
# Enter a number: 5
# 25

#
# number = int(input("Enter your value: "))
#
# while number > 31:
#     number = int(input("Enter a number lesser than 32: "))
#
# if number < 32:
#     for i in range(0, number + 1):
#         print("2 ^", i, " = ", 2**i)

user_input = input("Enter a number : ")

def get_square(user_input):
    return(user_input*user_input)

def get_input(user_input):
        try:
            get_square(user_input)
        except (TypeError, ValueError):
            while type(user_input) != int:
                print("Enter a valid input")
                user_input = input("Enter a number : ")

get_input(user_input)


#
# try:
#     number = int(user_input)
#     get_square(user_input)
# except ValueError:
#     while type(user_input) != int:
#         print("Enter a valid input")
#         user_input = input("Enter a number : ")
#         print(user_input, type(user_input))
#         # if type(user_input) == int:
#         #     number = int(user_input)
#         #     get_square(number)