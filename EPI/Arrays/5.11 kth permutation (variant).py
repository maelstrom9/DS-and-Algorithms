import math

def kth_permuatation(n,k):
    ## Adjust k according the index needed..
    k-=1
    ## why we do it?
    ## when n=4, this table works out for first place,
    ## 0-5 : 0
    ## 6-11: 1
    ##12-17: 2
    ##18-23: 3  ##Now if I want 16th that means (16-1)/6..gives me quotient 2 arr[2] is my req no.
    ##Note 1, 6 above means 3!
    ##Note 2, remainder left is carried forward..
    arr = [i for i in range(n)]
    res = []
    for i in range(n-1,-1,-1):
        index, k = divmod(k,factorial(i))
        res.append(arr[index])
        arr.remove(arr[index])
    return res
## space O(n) ..rec stack+res+arr...
## time O(n^2)...remove op is o(n)*o(n) loop...


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))
print(kth_permuatation(4,16))