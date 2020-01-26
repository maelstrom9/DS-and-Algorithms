

## key is figuring out how to check for intersection and then form a union.

def merging_intervals(arr,new):

    s,e = new
    new_arr = []

    i = 0
    if e<arr[0][0]:
        return [new]+arr
    elif s>arr[-1][1]:
        return arr+[new]
    else:
        i = 0
        while i<len(arr):
            si,ei = arr[i]
            if si<=s<=ei or si<=e<=ei or s<=si<=e or s<=ei<=e:
                while i<len(arr) and (si<=s<=ei or si<=e<=ei or s<=si<=e or s<=ei<=e):
                    s,e  = min(s,si),max(e,ei)
                    i+=1
                    if i<len(arr):
                        si, ei = arr[i]
                new_arr.append((s,e))
            else:
                new_arr.append((si,ei))
                i+=1
    return new_arr


res = merging_intervals([(-4,-1),(0,2),(3,6),(7,9),(11,12),(14,17)],(-5,8))
print(res)
res = merging_intervals([(-4,-1),(0,2),(3,6),(7,9),(11,12),(14,17)],(-5,-4))
print(res)
res = merging_intervals([(-4,-1),(0,2),(3,6),(7,9),(11,12),(14,17)],(-6,-5))
print(res)
res = merging_intervals([(-4,-1),(0,2),(3,6),(7,9),(11,12),(14,17)],(-5,19))
print(res)