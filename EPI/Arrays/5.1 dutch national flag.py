


def partition(arr,pivot_index):
    val = arr[pivot_index]
    start, move = 0, 0
    end = len(arr)-1
    while start<end and move<=end:
        if arr[move]<val:
            if move!=start:
                arr[move],arr[start] = arr[start],arr[move]
            start+=1
            move+=1
        elif arr[move]==val:
            move+=1
        else:
            arr[end],arr[move] = arr[move],arr[end]
            end-=1
    return arr

print(partition([2,0,1],2))