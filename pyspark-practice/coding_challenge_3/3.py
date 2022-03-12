# We have a string which contains grocery items. Print these items in a comma-separated sequence after sorting them alphabetically.
# grocery_items = ' Grated Cheese, Coffee Powder, Pickles White Chocolate, Dark Chocolate, Eggs, Breads, Milk, Sugar, Salt, Cat Food, Fries'
# Expected Output:
# Breads, Cat Food, Coffee Powder, Dark Chocolate, Eggs, Fries, Grated Cheese, Milk, Pickles White Chocolate, Salt, Sugar


grocery_items = ' Grated Cheese, Coffee Powder, Pickles White Chocolate, Dark Chocolate, Eggs, Breads, Milk, Sugar, Salt, Cat Food, Fries'

words = grocery_items.split(",")
words.sort()
joined_string = ",".join(words)
print(joined_string)
