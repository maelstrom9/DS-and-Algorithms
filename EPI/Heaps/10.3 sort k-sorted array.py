
from heapq import heappush,heappushpop,heappop

def sort_k_sorted(arr,k):

    # form heap of size k
    # h = arr[:k]
    # heapify(h) ## only this step costs O(k)
    ## Instead of this add elements one by one..
    ## which would result in a better time complexity? yes log(n) n elements in tree
    h = []

    for i in arr[:k]:
        heappush(h,i)

    # arr[0] = heappop(h) ## O(logk)
    index = 0

    for i in arr[k:]:
         ## O(logk)
        arr[index] = heappushpop(h,i)
        index+=1

    while h:
        arr[index] = heappop(h)
        index+=1

    return arr

## time : O(nlogk) space: O(k)

a = [3,-1,2,6,4,5,8]

print(sort_k_sorted(a,2))
