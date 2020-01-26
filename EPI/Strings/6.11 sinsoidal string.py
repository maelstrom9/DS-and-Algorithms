

def sinsoid_string(s):

    res = []

    i = 1
    while i<len(s):
        res.append(s[i])
        i+=4
    i = 0
    while i<len(s):
        res.append(s[i])
        i+=2
    i = 3
    while i < len(s):
        res.append(s[i])
        i += 4


    return "".join(res)

print(sinsoid_string(["H","e","l","l","o","_","w","o","r","l","d"]))
