# Write a program to reverse words in a string.
# sample_text = "Python is a high-level and general-purpose programming language"
# Expected Output:
# language programming general-purpose and high-level a is Python

sample_text = "Python is a high-level and general-purpose programming language"

words = sample_text.split(' ')

reverse_text = ' '.join(reversed(words))

print(reverse_text)