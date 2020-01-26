import random
from collections import Counter

def rand7():
    return random.randint(1,7)


def rand10():
    res = 100
    while res>40:
        res = (rand7()-1)*7+rand7()
    return 1+(res-1)%10


print(rand10())

a = []
for i in range(100):
    a.append(rand10())

c = Counter(a)
print(c)
