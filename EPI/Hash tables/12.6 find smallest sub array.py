


a = ["I","ate","an","apple","and","then","I","slept"]
sub = ["ate","I"]


## update e and stop when dict keys == set keys
## update s until dict keys!=set keys, update distance as well

def smallest_sub_array(arr,sub):

    dist = (float('inf'),None,None)

    s,e = 0,0
    temp = {}

    while s<=e and s<len(arr):
        if set(temp.keys()) != set(sub) and e<len(arr):
            if arr[e] in sub:
                temp[arr[e]] = temp.get(arr[e],0)+1
            e+=1
        else:
            if set(temp.keys()) == set(sub):
                dist = min(dist,(e-s,s,e-1))

            if arr[s] in sub:
                if temp[arr[s]]==1:
                    del temp[arr[s]]
                else:
                    temp[arr[s]]-=1

            s+=1

    return dist


c = ["I","a","up","ok", "a","the","ar","up","a","a"]
sub2 = ["up","the","a"]

res = smallest_sub_array(c,sub2)

print(res)





