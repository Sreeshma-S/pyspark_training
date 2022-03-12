# Write a Python function to find 'Mall' from the dictionary 'map_details' given below.
# map_details = {101:'Park', 102:'Zoo', 103:'Mall'}
# Expected Output:
# 103

map_details = {101:'Park', 102:'Zoo', 103:'Mall'}

for key, value in map_details.items():
    if value == 'Mall':
        print(key)
