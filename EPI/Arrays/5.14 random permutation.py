import random


def random_permutation(n):
    arr = [i for i in range(n)]
    r = n
    while n>1:
        index = get_index(r,n)
        arr[n-1], arr[index] = arr[index], arr[n-1]
        n-=1
    return arr

## used rejection sampling technique..
def get_index(r,n):
    rand_index = random.randint(1, r)
    quo, rem = divmod(r, n)
    if rand_index > n * quo:
        return get_index(r,n)
    else:
        return (rand_index-1)%n


print(random_permutation(7))