


def get_pivot(arr,s,e):
    while s<e:
        if arr[s][1]>arr[e][1]:
            arr[s],arr[e-1] = arr[e-1],arr[s]
            arr[e],arr[e-1] = arr[e-1],arr[e]
            e-=1
        else:
            s+=1
    return e


def get_median(arr,s,e,k):

    pivot = get_pivot(arr,s,e) ## this changes array also as it is passed as global variable.

    if sum([i[0] for i in arr[:pivot]])<k<sum([i[0] for i in arr[:pivot+1]]):
        return arr[pivot]
    elif sum([i[0] for i in arr[:pivot+1]])<k:
        return get_median(arr,pivot+1,e,k)
    else:
        return get_median(arr,s,pivot-1,k)


# a = [(10,1),(1,3),(11,4),(20,5),(10,10),(16,6),(100,2)]
# a = [(3,1),(3,2),(2,3),(2,10)]
a = [(10,1),(30,2),(20,5),(5,70)]
print(sum([i[0] for i in a])//2)


print(sorted(a,key = lambda x:x[1]))

print(get_median(a,0,len(a)-1,sum([i[0] for i in a])//2))


1,1,1,2,2,2,3,3,10,10
