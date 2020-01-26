

def multiply(arr1,arr2):
    sign = -1 if arr1[0]<0 ^ arr2[0]<0 else +1

    n = len(arr1)
    m = len(arr2)

    res = [0]*(n+m)

    i = 0
    for x in reversed(arr1):
        c = 0
        j = 0
        for y in reversed(arr2):
            m = x*y
            r = res[i+j]+m+c
            res[i+j] = (r%10)
            c = (r)//10
            j+=1
        if c!=0:
            res[i+j]=c
        i+=1
    while res[-1]==0:
        res = res[:-1]
    return res[::-1] ##need to put a sign as ewll.

print(11*3)
print(multiply([3],[1,1]))

