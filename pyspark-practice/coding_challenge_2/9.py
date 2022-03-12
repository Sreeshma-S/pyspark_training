# Here we have a poem by Walt Whitman. I want you to print this poem once again after removing all the vowels from them.
# poem = "Centre of equal daughters, equal sons,
# All, all alike endeared, grown, ungrown, young or old,
# Strong, ample, fair, enduring, capable, rich,
# Perennial with the Earth, with Freedom, Law and Love,
# A grand, sane, towering, seated Mother,
# Chaired in the adamant of Time."
# Expected Output:
# 'Cntr f ql dghtrs, ql sns,All, ll lk ndr’d, grwn, ngrwn, yng r ld,Strng, mpl, fr, ndrng, cpbl, rch,Prnnl wth th Erth, wth Frdm, Lw nd Lv,A grnd, sn, twrng, std Mthr,Chr’d n th dmnt f Tm.'


poem = "Centre of equal daughters, equal sons, All, all alike endeared, grown, ungrown, young or old, Strong, ample, fair, enduring, capable, rich, Perennial with the Earth, with Freedom, Law and Love, A grand, sane, towering, seated Mother, Chaired in the adamant of Time."

for j in ['a', 'e', 'i', 'o', 'u']:
    s1 = poem.replace('e','')
    s2 = s1.replace('a', '')
    s3 = s2.replace('i', '')
    s4 = s3.replace('o', '')
    s = s4.replace('u', '')
print(s)

