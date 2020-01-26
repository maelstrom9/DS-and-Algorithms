




def duplicate_missing_elements(arr):

    s=0
    d=0
    n = len(arr)

    for i in range(len(arr)):
        if arr[arr[i]]<0:
            d = arr[i]
        else:
            arr[arr[i]]=-arr[arr[i]]
        s+=abs(arr[i])

    m = n*(n-1)/2
    # m = m+d-s
    print(m,d,s)
    return d,m+d-s

a = [0,1,1,4,3,2]

print(duplicate_missing_elements(a))

