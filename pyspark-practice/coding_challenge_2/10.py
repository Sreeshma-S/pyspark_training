# Here we have some information about Python programming extracted from Wikipedia.
# Find all the occurrences of the word 'python' in the given python_info, ignoring the case.
#
# python_info = "Python is an interpreted, high-level, and general-purpose programming language.
# Python is dynamically typed and garbage-collected.
# Python was created in the late 1980s as a successor to the ABC language, Python 2.0.
# Python 3.0 was released in 2008.
# A non-profit organization, the Python Software Foundation, manages and directs resources for Python development."
# Expected Output:
# The 'Python' count in python_info is: 7

python_info = "Python is an interpreted, high-level, and general-purpose programming language. Python is dynamically typed and garbage-collected. Python was created in the late 1980s as a successor to the ABC language, Python 2.0. Python 3.0 was released in 2008. A non-profit organization, the Python Software Foundation, manages and directs resources for Python development."

count = 0
for i in python_info.split(' '):
    if i.lower() == 'python':
        count += 1
print("The 'Python' count in python_info is: ", count)
