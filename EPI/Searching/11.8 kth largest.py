


def get_pivot(arr,s,e):
    while s<e:
        if arr[s]>arr[e]:
            arr[s],arr[e-1] = arr[e-1],arr[s]
            arr[e],arr[e-1] = arr[e-1],arr[e]
            e-=1
        else:
            s+=1
    return e

def k_th_largest(arr,s,e,k):
    pivot = get_pivot(arr,s,e)

    if pivot==k-1:
        return arr[pivot]
    elif pivot>k-1:
        return k_th_largest(arr,s,pivot-1,k)
    else:
        return k_th_largest(arr,pivot+1,e,k)

def get_kth_largest(arr,k):
    if not arr or k>len(arr):
        return -1
    return k_th_largest(arr,0,len(arr)-1,len(arr)-k+1)

arr = [1,11,2,6,12,9,8,-1,1,1,1]
print(get_kth_largest(arr,11))
print(sorted(arr))