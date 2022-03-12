# Convert the string given below into a list by taking each word separated by a comma as an element.
# languages = "Java, Python, C++, Scala, C"
# Expected Output:
# ['Java', ' Python', ' C++', ' Scala', ' C']


languages = "Java, Python, C++, Scala, C"

languages_new_list = languages.split(",")

print(languages_new_list)