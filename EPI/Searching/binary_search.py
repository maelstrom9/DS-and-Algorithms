
from bisect import bisect_right,bisect_left

def binary_search(arr,x):
    # empty array:
    if not arr:
        return -1

    s = 0
    e = len(arr)-1

    while s<=e:
        # mid = (s + e) // 2   ### s+e might cause overflow...typical bug in programs.
        mid = s+ (e-s)//2
        if arr[mid] == x:
            return mid,x
        elif arr[mid]>x:
            e = mid-1
        else:
            s = mid+1
    return -1


a = [1,1,2,2,3,4,5,11,15,17,22,100]

print(binary_search(a,2))

print(bisect_right(a,2)) ## first entry greater than 2....if all less return len(a)

print(bisect_left(a,6))

print(bisect_left(a,2))  ## first entry greater than or equal to 2.... if all less or eq returns len(a)


s = ["ab","bc","ce","r","rx","ztc"]
print(binary_search(s,"c"))