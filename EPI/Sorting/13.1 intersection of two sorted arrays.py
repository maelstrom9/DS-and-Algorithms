



def intersection_sorted_arrs(arr1,arr2):

    s1, s2 = 0,0
    c = 0
    res = []
    while s1<len(arr1) and s2<len(arr2):
        if c%2:
            while s2<len(arr2) and arr2[s2]<=arr1[s1]:
                s2+=1
            if s2!=0 and arr2[s2-1] == arr1[s1]:
                res.append(arr1[s1])
        else:
            while s1<len(arr1) and arr1[s1]<=arr2[s2]:
                s1+=1
            if s1!=0 and arr1[s1-1] == arr2[s2]:
                res.append(arr2[s2])

        c+=1
    return res



## lol this is nlog(n)..  O(n+m) should be possible.

import bisect

def intersection_sorted_arrays(arr1,arr2):

    s1, s2 = 0,0
    c = 0
    res = []
    while s1<len(arr1) and s2<len(arr2):
        if c%2:
            s2 = bisect.bisect_right(arr2,arr1[s1])
            if s2!=0 and arr2[s2-1]==arr1[s1]:
                res.append(arr1[s1])
        else:
            s1 = bisect.bisect_right(arr1, arr2[s2])
            if s1 != 0 and arr1[s1 - 1] == arr2[s2]:
                res.append(arr2[s2])
        c+=1

    return res


res = intersection_sorted_arrs([2,3,3,5,5,6,7,7,8,12],[5,5,6,8,8,9,10,10,12])

print(res)