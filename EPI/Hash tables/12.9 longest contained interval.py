



def l_interval(arr):

    arr = set(arr)
    d = float("-inf")

    while arr:
        e= arr.pop()

        r,l = e,e
        while l-1 in arr:
            arr.remove(l-1)
            l-=1
        while r+1 in arr:
            arr.remove(r+1)
            r+=1

        d = max(d,r-l+1)
    return d


## O(d) d is distinct n, while below is O(dlogd)

### This solution is not optimal as it accounts for ordering of the set/list which is not optimal.

## NO NEED OF ORDERING>..ALWAYS THINK OF THIS...DO I REALLY NEED TO ORDER THE ELEMENTS??

## Another important thing is set or dictioanary or hash table look and delete are O(1).....

'''def l_interval(arr):

    if not arr:
        return 0

    arr = list(set(arr)) ## O(n)

    arr.sort() ## O(dlogd)

    s = 0
    d = (float('-inf'),s)
    for e in range(1,len(arr)):
        if arr[e]!=arr[e-1]+1:
            s = e
        d = max(d,(e-s+1,s))
        # print(d)

    return arr[d[1]:d[1]+d[0]+1]'''

print(l_interval([3,-2,7,9,8,1,2,0,-1,5,8]))



