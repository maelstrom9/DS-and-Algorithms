


def first_great(arr,k):

    if not arr:
        return -1

    s = 0
    e = len(arr)-1

    idx = -1

    while s<=e:
        m = s + (e-s)//2

        if arr[m]<=k:
            s = m+1
        elif arr[m]>k:
            e = m-1
            idx = m

    return idx

a = [-14,-10,2,108,108,243,285,285,285,401]

b = [1,2,4,4,5,7,11,12,13,140]
print(first_great(a,108))



def local_minima(arr):

    s = 0
    e = len(arr)-1

    while s<=e:

        m = s + (e-s)//2

        if m==0 or m==len(arr)-1 or(0<m<len(arr)-1 and arr[m]<=arr[m-1] and arr[m]<=arr[m+1]):
            return m
        elif arr[m]>arr[m-1]:
            e = m-1
        else:
            s = m+1


a = [10,12,13,41,40,5,2,1,6,18]
print(local_minima(a))

def get_interval(arr,k):
    if not arr: return [-1,-1]
    def get_lower_bound(arr,k):
        s,e = 0,len(arr)-1
        idx = -1
        while s<=e:
            m = s + (e-s)//2
            if arr[m]==k:
                idx = m
                e = m-1
            elif arr[m]<k:
                s = m+1
            else:
                e = m-1
        return idx

    def get_upper_bound(arr, k):
        s, e = 0, len(arr) - 1
        idx = -1
        while s <= e:
            m = s + (e - s) // 2
            if arr[m] == k:
                idx = m
                s = m + 1
            elif arr[m] < k:
                s = m + 1
            else:
                e = m - 1
        return idx
    return [get_lower_bound(arr,k),get_upper_bound(arr,k)]


c = [1,2,4,4,4,4,4,4,4,5,6,7,8]
d = []
print(get_interval(d,4)) ## test case 1
print(get_interval(d,12)) ## test case 2
print(get_interval(c,4)) ## test case 3


