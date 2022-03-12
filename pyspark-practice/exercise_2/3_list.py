# There is a list given below which contains the name of cities.
# Repeat this list of cities three times, and print the old list and the new list.
# cityList = ['London', 'New York', 'Delhi']
# Expected Output:
# Old City List: ['London', 'New York', 'Delhi']
# New City List: ['London', 'New York', 'Delhi', 'London', 'New York', 'Delhi', 'London', 'New York', 'Delhi']

cityList = ['London', 'New York', 'Delhi']

new_city_list = []
for i in range(0, 3):
    for j in cityList:
        new_city_list.append(j)

print("Old City List : {}".format(cityList))
print("New City List : {}".format(new_city_list))

