

## this is flawed solution...
def advance_array_game(arr):
    req = 1
    v = True

    for i in arr[::-1][1:]:
        if i>=req:
            req = 1
            v = True
        else:
            req+=1
            v = False
    return v

def advance_arr_game(arr):
    max_reach = 0
    index = 0
    while index<len(arr):
        if max_reach<index:
            return False
        max_reach = max(index+arr[index],max_reach)
        index+=1
    return True


a = [1,2,3,4]
print(advance_arr_game([3,3,0,0,2,0,1]))