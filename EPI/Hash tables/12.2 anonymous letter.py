

from collections import Counter

def anon_letter(s1,s2):

    if not s1:
        return True

    c1 = Counter(s1)

    for char in s2:
        if char in c1:
            c1[char]-=1
            # print(c1)
            if c1[char]==0:
                del c1[char]
        # print(c1)
        if len(c1)==0:  ## if not c1 is more pythonic...
            return True

    # for key in c1.keys():
    #     if c1[key]>c2[key]:
    #         return False
    return False

print(anon_letter("abc","rabcd"))

print(anon_letter("",""))

print(anon_letter("abc",""))

print(anon_letter("anana","asnnannnaaaaa"))