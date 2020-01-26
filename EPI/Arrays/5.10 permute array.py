

def permute(arr,per):
    for i in range(len(per)):
        while i!=per[i]:
            k = per[i]
            # print(per[i],per[per[i]])
            per[i],per[k] = per[k],per[i]
            arr[i],arr[k] = arr[k],arr[i]
    return arr

print(permute([10,9,8,12,24],[2,1,0,4,3]))