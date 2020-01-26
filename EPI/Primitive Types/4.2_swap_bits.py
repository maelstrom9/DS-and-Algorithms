

## O(1) but book's well written and simple
## bitmask **

def swap_bits(x,i,j):
    if (x&1<<i) ^ (x&1<<j):
        if x&1<<i:
            x = x&~(1<<i)
            # print(bin(x))
            x = x|1<<j
            # print(bin(x))
        else:
            x = x & ~(1<< j)
            # print(bin(x))
            x = x | (1 << i)
            # print(bin(x))
        return x

print(bin(swap_bits(8,0,3)))