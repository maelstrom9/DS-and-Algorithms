
from heapq import heapify,heappop

def merge_sorted_arrays(arrs):


    # initialize heap to no arrs and their starting elements
    h = [(j[0],i,0) for i,j in enumerate(arrs)]
    print(h)

    # heapify
    heapify(h)
    print(h)

    res = []

    while len(res)<sum([len(i) for i in arrs]):
        m = heappop(h)
        res.append(m[0])
        if m[2]<len(arrs[m[1]])-1:
            h.append((arrs[m[1]][m[2]+1],m[1],m[2]+1))
            heapify(h)
    return res


res = merge_sorted_arrays([[9,10],[3,4],[5,6,7,11]])

print(res)

