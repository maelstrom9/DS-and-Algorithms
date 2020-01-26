
## Brute force O(n)

# def parity(x):
#     result = 0
#     while x:
#         result ^= x &1
#         x>>=1
#     return result


## caching?

## division property

def parity(x):
    x^=x>>32
    x^=x>>16
    x ^= x >> 8
    x ^= x >> 4
    x^=x>>2
    x^=x>>1
    return x & 0x1

print(parity(10))

print(0x1)