
## very badly written.. need to take ideas from book..
'''def next_permutation(per):
    ## traverse from end to the point where there is no increase in the suffix
    i = len(per)-1
    while True:
        i-=1
        if per[i]<per[i+1]:
            break
    if i==-1:
        return []
    else:
        ## find the swap
        swap = False
        for s in range(i+1,len(per)-1):
            if per[s+1]<per[i]:
                per[s],per[i] = per[i],per[s]
                swap = True
                break
        if not swap: per[len(per)-1],per[i] = per[i],per[len(per)-1]
        # return per
        return per[:max(1,i)]+per[i+1:][::-1]

print(next_permutation([0,1,3,4,2]))'''


def next_permutation(arr):
    i = len(arr)-2
    while i>=0:
        if arr[i]<arr[i+1]:
            break
        i-=1
    ## last one..
    if i==-1:
        return []

    swap1 = i
    ## find the least possible from (the vals greater than it) from i+1
    # swapped = False
    # for i in range(swap1+1,len(arr)-1):
    #     if arr[swap1]>arr[i]:
    #         swapped = True
    #         break
    #
    # if not swapped:
    #     swap2 = len(arr)-1
    # else:
    #     swap2 = i-1
    #
    # ##swap
    # arr[swap1],arr[swap2] = arr[swap2],arr[swap1]

    for i in range(len(arr)-1,swap1,-1):
        if arr[i]>arr[swap1]:
            arr[swap1],arr[i] = arr[i],arr[swap1]
            break

    ## reverse and return..
    return arr[:swap1+1]+arr[swap1+1:][::-1]

print(next_permutation([0,1,3,4,2]))


## book one..updated above..
## The idea is to find the first one from reverse where that is greater than our swap1.


