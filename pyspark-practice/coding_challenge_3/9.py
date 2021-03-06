# We have a list of several names along with their age.
# Now, there is a meeting where seats are reserved for senior citizens (age - 45 above).
# I want to filter out the senior citizens from this list and get a resultant list where we the names of all those who satisfy the criteria.
# passenger_list = {
# 'Ross' : 35,
# 'Thomas': 42,
# 'Rick' : 55,
# 'Ericson' : 51,
# 'Josh' : 45,
# 'Lara' : 50,
# 'Emma' : 38,
# 'Lily' : 46,
# 'Ron' : 41,
# 'Michael' : 47,
# 'Joanna' : 56,
# 'Arthur' : 42
# }
# Expected Output:
# {'Rick', 'Lily', 'Ericson', 'Joanna', 'Michael', 'Lara'}


passenger_list = {
'Ross' : 35,
'Thomas': 42,
'Rick' : 55,
'Ericson' : 51,
'Josh' : 45,
'Lara' : 50,
'Emma' : 38,
'Lily' : 46,
'Ron' : 41,
'Michael' : 47,
'Joanna' : 56,
'Arthur' : 42
}

senior_passengers = []
for key, value in passenger_list.items():
    if value > 45:
        senior_passengers.append(key)
print(set(senior_passengers))

# sorted_banks = {}
# for key, value in sorted(stock_market.items(), key=lambda item:item[1]):
#     sorted_banks[value] = key
# print(sorted_banks)