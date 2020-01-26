

## Im loving this!! Nice fucking start.
def buy_sell_atmost_k(arr,k):

    P = [[0]*(len(arr)) for i in range(k+1)] ## nk space

    ## to avoid nk space make space of old P's and update new ones based on that..

    ## nk time
    for t in range(1,k+1):
        local_max = -arr[0]
        for d in range(1,len(arr)):
            local_max = max(local_max,-arr[d-1]+P[t-1][d-1])
            P[t][d] = max(P[t][d-1],arr[d]+local_max)

    return P[k][len(arr)-1]

print(buy_sell_atmost_k([12,11,13,9,12,8,14,13,15],1))

