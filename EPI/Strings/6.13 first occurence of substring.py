
import functools

## flawed solution.....

def first_occurence(sub,s):

    m,n = len(sub),len(s)
    if m>n:
        return -1

    i = 0
    j = 0
    while i<len(s)-len(sub)+1:
        while i<len(s) and j<len(sub) and s[i] == sub [j]:
            i+=1
            j+=1
        if j==m:
            return i-m
        else:
            i+=1
            j = 0

    return -1

# print(first_occurence("dadaas","dadaadadaadadaas"))
#
# print(first_occurence("eef","aeeefeeffgh"))
#
# print(ord("a"))


def string_hash(s,modulus):
    MULT  = 997
    return functools.reduce(lambda v,c:(v*MULT+ord(c))%modulus,s,0)

print((7-ord('a')%10)*997+98)
print(string_hash("bc",10))