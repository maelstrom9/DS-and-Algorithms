

def look_and_say(n):
    start = "1"
    for i in range(n-1):
        start = next(start)
    return start



def next(s):
    res = []  ## if string is used, every time new memory is allocated increasing the time complexity..
    count = 1
    # prev = s[0]
    # if len(s)==1:
    #     return str(count)+prev
    # for c in s[1:]:
    #     if c == prev:
    #         count+=1
    #     else:
    #         res .append(str(count)+prev)
    #         prev = c
    #         count = 1

    ## ELEGANT THAN ABOVE SNIPPET####

    i = 0
    while i<len(s):
        c = 1
        while i+1<len(s) and s[i]==s[i+1]:
            i+=1
            c+=1
        res.append(str(c)+s[i])
        i+=1
    return "".join(res)


print(look_and_say(7))