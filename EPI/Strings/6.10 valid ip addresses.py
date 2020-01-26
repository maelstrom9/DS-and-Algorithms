

## 19216811

## assumin ip as char array
def all_valid_ips(ip,c,d,res):
    if c == len(ip)-1:
        return ["".join(res)]

    if d==3 and ip[c]!="0":
        return ["".join(res)+"".join(ip[c:])]

    temp = []
    if ip[c+1]!=0 and d<3:
        for i in range(1,4):
            if c+i<len(ip)-1:
                temp.extend(all_valid_ips(ip,c+i,d+1,res+ip[c:c+i]+["."]))

    return temp

print(all_valid_ips(list("192106811"),0,0,[]))

