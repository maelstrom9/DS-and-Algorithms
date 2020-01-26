




## optimal

def min_max_simul(arr):

    if not arr:
        return -1,-1

    g_min = float("inf")
    g_max = float("-inf")

    i = 0
    while i<len(arr):
        if i+1<len(arr):
            mi,ma = (arr[i],arr[i+1]) if arr[i]<=arr[i+1] else (arr[i+1],arr[i])
            g_min = min(mi,g_min)
            g_max = max(ma,g_max)
            i+=2
        else:
            g_min = min(arr[i], g_min)
            g_max = max(arr[i], g_max)
            i+=1
    return g_min,g_max

a = [3,1,4,2,20,11,3,25,-1]
print(min_max_simul(a))






## optimal but not enough...

def min_max_simulataneous(arr):

    if not arr:
        return -1,-1

    mi = arr[0]
    ma = arr[0]

    for e in arr[1:]:
        if e<=mi:
            mi = e
        else:
            ma = max(e,ma)

    return mi,ma

# a = [3,1,4,2,20,11,3,25]
# print(min_max_simulataneous(a))
