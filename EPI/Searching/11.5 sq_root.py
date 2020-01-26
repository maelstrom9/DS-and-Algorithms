
import math

def sq_root(no):

    s = 1
    e = no
    res = 1

    while s<=e:
        m = s + (e-s)//2

        if m**2>no:
            e = m-1
        elif m**2==no:
            return m
        else:
            res = m
            s = m+1
    return s-1

print(sq_root(17))


def real_sq_root(no):

    ## key idea
    s, e = (no,1) if no<1 else (1,no)

    while not math.isclose(s,e):
        m = s + (e-s)/2.0
        if m**2>no:
            e = m
        else:
            s = m
    return s

print(real_sq_root(0.17)**2)

def variant(x,y):
    ## key idea
    s, e = (1, x) if x > y else (0, 1)

    while not math.isclose(s, e):
        m = s + (e - s) / 2.0
        if m * y > x:
            e = m
        else:
            s = m
    return s

print(variant(22,10))