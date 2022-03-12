# We have a string that contains the names of different fruits.
# I want you to convert this string into multiple substrings where each substring includes one fruit's name.
# fruits_string = " Apple, Banana, Mango, Kiwi, Guava, Grapes, Pomegranate, Orange, Watermelon"
# Expected Output:
# Apple
# Banana
# Mango
# Kiwi
# Guava
# Grapes
# Pomegranate
# Orange
# Watermelon

fruits_string = " Apple, Banana, Mango, Kiwi, Guava, Grapes, Pomegranate, Orange, Watermelon"
fruits_list = fruits_string.split(",")
for a in fruits_list:
    print(a)