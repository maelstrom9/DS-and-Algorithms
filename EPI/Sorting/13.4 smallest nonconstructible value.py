


## Idea is to see if the difference between the max possible so far and the next element should be at max 1.

def smallest_not_constructible_value(arr):

    if not arr:
        return -1

    # arr.sort() # O(nlogn)

    M = 0
    # if M != 1: return 1

    for i in sorted(arr):
        if i<=M+1:
            M = i+M
        else:
            return M+1

print(smallest_not_constructible_value([1,1,1,1,1,5,10,25]))







## brute force
def smallest_non_constr_value(arr):

    pos_val = [0]

    for i in arr:
        temp = []
        for j in pos_val:
            temp.append(i+j)
        pos_val.extend(temp)

    pos_val = list(set(pos_val))

    pos_val.sort()

    for i in range(1,len(pos_val)):
        if pos_val[i]!=pos_val[i-1]+1:
            return pos_val[i-1]+1
    return pos_val[-1]+1


print(smallest_non_constr_value([1,5,10,11,25]))


