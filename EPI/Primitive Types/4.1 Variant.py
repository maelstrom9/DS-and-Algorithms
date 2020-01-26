#Right propagate the rightmost set bit in x, e.9., tums (01010000) to (01011111)


def right_propogate(x):
    return x|(x-1)


def ispower2(x):
    return x&(x-1)==0

def mod_power2(x,y):
    return x^y

def extract_lowest_set_bit(x):
    return x&~(x-1)

print(extract_lowest_set_bit(12))

print((mod_power2(8,4)))

print(bin(right_propogate(80)))
