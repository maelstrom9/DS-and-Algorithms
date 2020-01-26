

## easy peasy one..
def alternate(arr):
    for i in range(len(arr)-1):
        if i%2==0:
            if arr[i]<=arr[i+1]:
                continue
            else:
                arr[i],arr[i+1]= arr[i+1],arr[i]
        else:
            if arr[i]>=arr[i+1]:
                continue
            else:
                arr[i],arr[i+1]= arr[i+1],arr[i]
    return arr

print(alternate([7,6,5,4,3,2,1,10]))