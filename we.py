import enchant
d = enchant.Dict("en_US")
import itertools
str="dictionary"
Permutation=itertools.permutations(str,3)
for i in Permutation:
    str1="".join(i)
    if(d.check(str1)==True):
        print(str1)
