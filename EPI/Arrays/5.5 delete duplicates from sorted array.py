

## /Is deletion O(1)?? ## O(n^2)
def del_dups(arr):
    i = 0
    d = 0
    while i<len(arr)-1 and arr[i]!=0:
        if arr[i]!=arr[i+1]:
            i+=1
        else:
            del arr[i+1]
            arr.append(0)
            d+=1
    return arr[:len(arr)-d]

##O(n)
def del_dups2(arr):
    if not arr:
        return -1
    i=j=0
    d = 0
    prev = -1
    while j<len(arr):
        if arr[j]!=prev:
            arr[i] = arr[j]
            prev = arr[i]
            i+=1
            j+=1
        else:
            j+=1
            d+=1
    return arr[:len(arr)-d]


print(del_dups2([2,2,3,5,5,7,11,11,11,13,14,15,15]))