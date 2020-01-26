


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
    if not arr or k>len(arr) or k==0:
        return -1
    return k_th_largest(arr,0,len(arr)-1,len(arr)-k+1)


## Instead of 2 pass, find mid point then send the array s,m-1 to find m-1==k. for finding m-1...
def get_median(arr):
    if not arr:
        return -1
    if len(arr)%2 == 0:
        # print(k_th_largest(arr,0,len(arr)-1,len(arr)//2))
        return (k_th_largest(arr,0,len(arr)-1,len(arr)//2+1)+k_th_largest(arr,0,len(arr)-1,len(arr)//2))/2
    else:
        return k_th_largest(arr,0,len(arr)-1,len(arr)//2+1)

arr = [1,11,2,6,12,9,8,-1,87,3,99]
# print(get_kth_largest(arr,4))
print(sorted(arr),len(arr))
# print(get_kth_largest(arr,0))
print(get_median(arr))