

def encode(s):
    res  = []
    i = 0
    while i<len(s):
        c = 1
        while i+1<len(s) and s[i]==s[i+1]:
            c+=1
            i+=1
        res.append(str(c)+s[i])
        i+=1
    return "".join(res)

print(encode("aaaabccccccccccccccccccaa"))


def decode(s):
    res = []
    count = 0
    for c in s:
        if c.isdigit():
            count = count*10 + int(c)
        else:
            res.append(count*c)
            count = 0
    return "".join(res)

print(decode("31e11f2e"))