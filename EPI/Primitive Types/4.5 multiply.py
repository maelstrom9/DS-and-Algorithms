
## left shit y (2^k.y) at every set bit x and add them all.
def multiply(x,y):
    print(bin(x))
    s = 0
    k = 0
    while x:
        if x&1:
            s = add(s,y<<k)
        x = x>>1
        k+= 1
    return s


## adding two no.s .. carryin and carryout are the key things..and xor as well.
def add(a,b):
    print(bin(a))
    running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
    while temp_a or temp_b:
        ak, bk = a&k, b&k
        carryout = (ak&bk) |(ak&carryin)| (bk&carryin)
        running_sum |= ak^bk^carryin
        carryin, k, temp_a, temp_b = (carryout<<1,k<<1,temp_a>>1,temp_b>>1)

    return running_sum|carryin

print(add(22,22))