
from heapq import heappush,heappop

def k_larget_in_max_heap(h,k):


    rh = [(-h[0],0)]
    r = []

    while k:
        parent = heappop(rh)
        r.append(-parent[0])
        for i in [2*parent[1]+1,2*parent[1]+2]:
            if i <len(h):
                heappush(rh,(-h[i],i))
        k-=1

    return r

res = k_larget_in_max_heap([561,314,401,28,156,359,271,11,3],4)
print(res)


## time: O(klogk) space: O(k)