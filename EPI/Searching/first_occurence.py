


def first_occurence(arr,k):
    if not arr:
        return -1

    s = 0
    e = len(arr)-1
    idx = -1

    while s<=e:
        m = s+(e-s)//2

        if arr[m]==k:
            idx = m
            e = m-1 ## still do binary search ##
            ## O(n) no good ##
            # while m>=0 and arr[m-1]==k:
            #     m -=1
            # return m
        elif arr[m]>k:
            e = m-1
        else:
            s = m+1

    return idx

# a = [-14,-10,2,108,108,243,285,285,285,285,285,285,401]
a = [1,2,24,25,26,27,27,28,28]

res = first_occurence(a,28)
print(res)