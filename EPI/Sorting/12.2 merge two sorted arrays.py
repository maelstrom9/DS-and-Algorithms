




def merge_two_sorted_arrs(arr1,arr2):

    m = len(arr2)

    if not arr1 or not arr2:
        return arr1 or arr2

    i = arr1.index("_")-1
    j = len(arr2)-1
    k = r = i+m
    while i>=0 and j>=0:
        if arr1[i]>arr2[j]:
            arr1[k] = arr1[i]
            i-=1
            k-=1
        else:
            arr1[k] = arr2[j]
            j-=1
            k-=1

    ## this is not needed because this arr1 is already sorted
    # while i>=0:
    #     arr1[k] = arr1[i]
    #     i-=1
    #     k-=1

    while j>=0:
        arr1[k] = arr2[j]
        j-=1
        k-=1

    return arr1[:r+1]

res = merge_two_sorted_arrs([5,13,17,"_","_","_","_","_"],[3,7,11,19])
print(res)