import math

def reverse_digits(x):
    res = 0
    s = -1 if x<0 else +1
    x = abs(x)
    while x:
        rem = x%10
        res=res*10+rem
        x = (x-rem)//10
    return int(res)*s

print(reverse_digits(4422))



## Instead of recursion, (to avoid recursvive call stack..space complexity)
## Using a loop half the size of no.of digits is better.
def check_palindrome(x):
    if x<0:
        return False
    l = x%10
    n = math.floor(math.log(x,10))+1
    if n==1:
        return True
    # print(n)
    f = x//10**(n-1)
    print(l,f)
    if l!=f:
        return False
    else:
        x = (x-(f*10**(n-1))-l)//10
        print(x)
        check_palindrome(x)
    return True

print(check_palindrome(121))

