# We have a dictionary given below. Delete the item with key '3,' and add an item with key '7' and value 'Black.'
# color = {1:'Red', 2:'Orange', 3:'White', 4:'Brown', 5:'Yellow'}
# Expected Output:
# {1: 'Red', 2: 'Orange', 4: 'Brown', 5: 'Yellow', 7: 'Black'}


color = {1:'Red', 2:'Orange', 3:'White', 4:'Brown', 5:'Yellow'}

color_delete = color.pop(3)

color_insert = color[7] = 'Black'

print(color)