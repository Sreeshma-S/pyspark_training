# We have a list of companies with their face values in the stock market.
# Now, I want to get the company's name along with its face value for the company, which has the maximum and the minimum face values. ' \
# I also want you all to sort this list based on face values in increasing order.
# In this example, you have the flexibility to go ahead and google for some hints.
#
# stock_market = {
# 'AXIS BANK' : 7,
# 'BHARTI AIRTEL' : 5,
# 'COAL INDIA' : 10,
# 'ITC' : 1,
# 'TCS' : 3,
# 'L&T' : 2,
# 'RELIANCE' : 9,
# 'KOTAK BANK' : 8,
# 'AMERICAN EXPRESS' : 11
# }
#
# Expected Output:
# (1, 'ITC')
# (11, 'AMERICAN EXPRESS')
# [(1, 'ITC'), (2, 'L&T'), (3, 'TCS'), (5, 'BHARTI AIRTEL'), (7, 'AXIS BANK'), (8, 'KOTAK BANK'), (9, 'RELIANCE'), (10, 'COAL INDIA'), (11, 'AMERICAN EXPRESS')]

stock_market = {
'AXIS BANK' : 7,
'BHARTI AIRTEL' : 5,
'COAL INDIA' : 10,
'ITC' : 1,
'TCS' : 3,
'L&T' : 2,
'RELIANCE' : 9,
'KOTAK BANK' : 8,
'AMERICAN EXPRESS' : 11
}



for key, value in stock_market.items():
    all_values = stock_market.values()
    max_value = max(all_values)
    min_value = min(all_values)
    max_tuple = ()
    if value == max_value:
        max_tuple = key, max_value
        print(max_tuple)
    min_tuple = ()
    if value == min_value:
        min_tuple = key, min_value
        print(min_tuple)

sorted_banks = {}
for key, value in sorted(stock_market.items(), key=lambda item:item[1]):
    sorted_banks[value] = key
print(sorted_banks)
