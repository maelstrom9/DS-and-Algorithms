

## a -- 2d's
## b -- remove

def rep_and_remove(arr):

    ## first remove b

    ## start, write pointers
    w = 0
    count,count2 = 0,0
    for c in arr:
        if c=="b":
            count += 1
            continue
        elif c=="":
            count2+=1
        else:
            arr[w] = c
            w+=1

    if count+count2>0:
        for i in range(count+count2):
            arr[len(arr)-i-1] = ""
    print(arr)

    ##now work on a from backwards
    # w += count
    for c in reversed(arr):
        if c=="a":
            arr[w-1:w+1] = "dd"  ## This is interesting..
            w-=2
        elif c=="":
            continue
        else:
            arr[w] = c
            w-=1

    return arr

print(rep_and_remove(["a","d","b","c","",""]))

# a = [1,2,3,4]
# # print(a[-2:-])
# print(a[-3:0])

