
from collections import Counter

def test_pal_per(s):

    c = Counter(s)
    r = 0
    for i in c.values():
        r += i%2

    return True if r==0 or r==1 else False


print(test_pal_per("abc"))
print(test_pal_per("abba"))
print(test_pal_per(""))
print(test_pal_per("lleei"))

print(len(""))
if "":
    print(1)
