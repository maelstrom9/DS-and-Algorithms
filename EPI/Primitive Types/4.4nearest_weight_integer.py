

def find_nearest_weight(x):
    lsb = x&1
    c = 1
    while True:
        # print(1<<c)
        # print(x>>c&1)
        if lsb^(x>>c&1)==1:
            break
        c+=1
    ## swap cth and c-1 th bits
    return swap_bits(x,c,c-1)


def swap_bits(x,i,j):
    if (x>>i)&1 != (x>>j)&1:
        bit_mask = (1<<i)|(1<<j)
        return x^bit_mask

print(find_nearest_weight(8))



## O(1)

def find_near_int(x):
    ## right most set bit
    rs = x&~(x-1)
    ##right most non set bit
    rns = (~x)&~(~x-1)
    if rs>rns:
        bitmask = rs|rs>>1 
    else:
        bitmask = rns|rns>>1
    return bitmask^x

print(find_near_int(8))