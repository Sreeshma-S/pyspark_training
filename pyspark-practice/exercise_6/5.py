# We have the names of six countries given below.
# Write a Python function to print all the countries that start with the letter 'A.'
# 'Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran'
# Expected Output:
# ['Austraiia', 'Austria', 'America']

countries = 'Austraiia', 'India', 'Austria', 'America', 'Russia', 'Iran'
countryList = list(countries)

new_country_list = []
for i in countryList:
    if 'A' in i:
        new_country_list.append(i)

print(new_country_list)