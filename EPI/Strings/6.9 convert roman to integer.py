

def roman2int(r):
    val = i = 0
    d = {}
    d["X"]=10
    d["I"]=1
    d["L"]=50
    d["M"]=1000
    d["V"]=5
    d["C"]=100
    d["D"]=500

    prev = 0
    idx = len(r)-1
    while idx>=0:
        if d[r[idx]]>=prev:
            val += d[r[idx]]
        else:
            val -= d[r[idx]]
        prev = d[r[idx]]
        idx-=1
    return val


print(roman2int("MMIX"))