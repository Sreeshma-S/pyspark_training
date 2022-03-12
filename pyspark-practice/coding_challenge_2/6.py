# Print all the prime numbers between the given range.
# start = 20
# end = 60
# Expected Output:
# Prime numbers between 20 and 60 are: 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59

prime_nos = []
for i in range(20, 60):
    # print(i)
    for j in range(2, i):
        if i % j == 0:
            prime_nos.append(i)

prime_nos_sorted = sorted(set(range(20, 60)) - set(prime_nos))

print("Prime numbers between 20 and 60 are: ")
for i in prime_nos_sorted:
    print(i)