

from heapq import heapify,heappush,heappop

def reorganize(arr):

    #alternate reorganize
    counts = {}
    for c in arr:
        counts[c] = counts.get(c,0)+1

    ## form heap of counts.
    counts = [(-v,k) for k,v in counts.items()]

    # for i in counts:
    #     if -i[0]>(len(arr)+1)/2:
    #         return ""

    heapify(counts)

    res = []
    while len(counts)>1:
        c1, ch1 = heappop(counts)
        c2, ch2 = heappop(counts)

        res.append(ch1)
        c1 += 1

        res.append(ch2)
        c2 +=1

        if c1<0:
            heappush(counts,(c1,ch1))
        if c2<0:
            heappush(counts,(c2,ch2))

    if len(counts)==1:
        if -counts[0][0]>1:
            return ""
        res.append(counts[0][1])

    return "".join(res)


res = reorganize("bbbrrrrarr")

print(res)
#
# a = [1,2,3]
# heapify(a)
#
# for i in range(4):
#     print(heappop(a))

import collections


## leetcode discuss lee answer.

def rearrangeString(s, k):
    n = len(s)
    if not k: return s
    cou = collections.Counter(s)
    maxf = max(cou.values())
    if (maxf - 1) * k + list(cou.values()).count(maxf) > len(s):
        return ""
    res = list(s)
    i = (n - 1) % k
    for c in sorted(cou, key=lambda i: -cou[i]):
        for j in range(cou[c]):
            res[i] = c
            i += k
            if i >= n:
                i = (i - 1) % k
    return "".join(res)



print(rearrangeString("abasdadncasssdaaddrrsas",k=3))
print(rearrangeString("abcdabcdabcdabcd",k=4))

# print("".join(["a","","b"]))





