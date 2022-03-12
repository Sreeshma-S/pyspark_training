# Convert the list given below into a string using a comma as a separator argument.
# myList = ['Lenovo', ' Dell', ' Acer', ' Asus', ' HP']
# Expected Output:
# 'Lenovo, Dell, Acer, Asus, HP'



myList = ['Lenovo', ' Dell', ' Acer', ' Asus', ' HP']

# str = ""
# for i in myList:
#     str += i + ","
# print(str)


joined_string = ",".join(myList)

print(joined_string)
