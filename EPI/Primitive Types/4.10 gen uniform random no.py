import random
import math
from collections import Counter


def rand_bin():
    return random.randint(0,1)

def rand_uniform(a,b):
    rang = b-a ## 0 is included
    n = math.floor(math.log(rang,2))+1 ## need n bits to capture "rang" numbers
    res = rang+1
    while res>rang:
        res = generate(n)
    return res+a

def generate(n):
    res = 0
    k = 0
    while n:
        res|=rand_bin()<<k
        k+=1
        n-=1
    return res


print(rand_uniform(1,6))

a = []
for i in range(10000):
    a.append(rand_uniform(1,7))

c = Counter(a)
print(c)


