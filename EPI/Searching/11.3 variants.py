
import bisect




def cyclic_sort(arr):

    if not arr:
        return -1

    s = 0
    e = len(arr)-1

    # res = 0

    while s<e:
        m = s + (e-s)//2

        if arr[m]>arr[s]:
            s = m+1
        else:
            # res = m ## more efficient is to not record res. and to include mid as end...
            e = m ## m is also a possible value

    return s

a = [377,378,380,103,203,220,234,279,368,370]

print(cyclic_sort(a))





def asc_des_max(arr):

    if not arr: return -1

    s = 0
    e = len(arr)-1

    while s<=e:
        m = s+ (e-s)//2

        if m==0 or m==len(arr)-1:
            return m

        if arr[m]>arr[m-1] and arr[m]>arr[m+1]:
            return m
        elif arr[m-1]<arr[m]<arr[m+1]:
            s = m+1
        elif arr[m-1]>arr[m]>arr[m+1]:
            e = m-1


a = [1,2,3,4,5,10,9,7,6,4]

print(asc_des_max(a))


def cyc_elem(arr,k):
    pivot = cyclic_sort(arr)

    if pivot == 0:
        return bisect.bisect_left(arr,k)
    if k>arr[0]:
        return bisect.bisect_left(arr[:pivot],k)
    else:
        return pivot+bisect.bisect_left(arr[pivot:],k)

a = [378,478,550,631,103,203,220,234,279,368]

print(cyc_elem(a,631))