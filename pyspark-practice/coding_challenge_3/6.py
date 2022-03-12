# We have the time in seconds given below. Convert this time into days, hours, minutes, and seconds.
# time = 996452
# Expected Output:
# Days : Hours : Minutes : Seconds -> 11 : 12 : 47 : 32

time = 996452
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("Days : Hours : Minutes : Seconds -> %d:%d:%d:%d" % (day, hour, minutes, seconds))
