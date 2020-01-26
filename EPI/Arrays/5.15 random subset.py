import random

# 0 1 2 3
# 2
# 2 1 0 3 A[0]=2, A[2]=0
# 2 i=1
# 2 0 1 3 A[0]=2,A[2]=1,A[1]=A[2]=0
# 2
# 2 1 0 3

def random_subset(n,k):
    updated  = {}

    for i in range(k):
        rand_idx = random.randint(i,n-1)
        ## key step
        rand_idx_mapped = updated.get(rand_idx,rand_idx)
        i_map = updated.get(i,i)
        ## swap operation...
        updated[i] = rand_idx_mapped
        updated[rand_idx] = i_map
    return [updated[i] for i in range(k)]

print(random_subset(10,5))