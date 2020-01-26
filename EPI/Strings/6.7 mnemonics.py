


def mnemonics(s,d,index,res):
    ## base cond
    if index==len(s):
        return [res]

    temp = []
    for c in d[s[index]]:
        temp.extend(mnemonics(s,d,index+1,res+c))

    return temp



## how to construct this dict is another question..
d = {}
d["2"] = ["A","B","C"]

print(mnemonics("22",d,0,""))