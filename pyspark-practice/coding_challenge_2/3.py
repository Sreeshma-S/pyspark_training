# Find out the number of letters and digits from the given alpha-numeric text.
# sample_text = "Learning Journal 2020"
# Expected Output:
# Number of Letters: 15
# Number of Digits: 4

sample_text = "Learning Journal 2020"

letters_count = 0
numbers_count = 0

for i in sample_text:
    if i.isnumeric():
        numbers_count += 1
    elif i.isalpha():
        letters_count += 1

print("Number of Letters: ", numbers_count)
print("Number of Digits: ", letters_count)