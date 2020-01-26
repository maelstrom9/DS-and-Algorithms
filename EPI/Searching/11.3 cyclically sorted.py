


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


