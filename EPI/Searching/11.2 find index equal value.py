
## this can be simplied to search on left and right only as below.
''' elif arr[m]>m:
     left = find_equal_index_val(arr,s,m-1)
     right = find_equal_index_val(arr,max(arr[m],m+1),e)
 else:
     left = find_equal_index_val(arr, s, min(m-1,arr[m]))
     right = find_equal_index_val(arr, m+1, e)'''

def find_equal_index_val(arr,s,e):

    ## base case
    if s>e:
        return -1

    m = s + (e-s)//2

    ## found condition
    if arr[m]==m:
        return m

    left = find_equal_index_val(arr, s, min(m - 1, arr[m]))
    right = find_equal_index_val(arr, max(arr[m], m + 1), e)

    if left >= 0: return left
    if right >= 0: return right
    return -1


def magic_index(arr):
    return find_equal_index_val(arr,0,len(arr)-1)

print(magic_index([-1,0,3,4,5,5,5,6,8,10]))
